# https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict
import heapq

# 다익스트라
def solution(n, paths, gates, summits):

    summits.sort()
    summits_set = set(summits)
 
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))


    q = []  # (intensity, 위치)
    visited = [10000001] * (n + 1)  # intensity 저장

    for gate in gates:
        heapq.heappush(q, (0, gate))
        visited[gate] = 0

    while q:
        intensity, node = heapq.heappop(q)

        # 산봉우리이거나 더 큰 intensity면 continue
        if node in summits_set or intensity > visited[node]:
            continue

        for weight, next_node in graph[node]:
            new_intensity = max(intensity, weight)  # intensity 갱신
            if new_intensity < visited[next_node]:
                visited[next_node] = new_intensity
                heapq.heappush(q, (new_intensity, next_node))

    min_intensity = [0, 10000001]
    for summit in summits:
        if visited[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]


    return min_intensity
