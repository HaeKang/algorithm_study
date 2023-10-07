
# https://www.acmicpc.net/problem/1504

import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    n1, n2, wgt = map(int, input().split())
    graph[n1].append([n2, wgt])
    graph[n2].append([n1, wgt])

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    dist = [1e9] * (n+1)

    dist[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        now_dist, now_node = heapq.heappop(q)

        if dist[now_node] < now_dist:
            continue

        for next_node, wgt in graph[now_node]:
            next_dist = now_dist + wgt

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])

    return dist


one_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = one_dist[v1] + v1_dist[v2] + v2_dist[n]
v2_path = one_dist[v2] + v2_dist[v1] + v1_dist[n]

ans = min(v1_path, v2_path)

if ans < 1e9:
    print(ans)
else:
    print(-1)
