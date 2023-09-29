# https://www.acmicpc.net/problem/5972

import sys
import heapq
input = sys.stdin.readline

# 1 -> n
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [1e9] * (n+1)

for _ in range(m):
    n1, n2, wgt = map(int, input().split())
    graph[n1].append([n2, wgt])
    graph[n2].append([n1, wgt])


q = []
heapq.heappush(q, [0, 1])
dist[1] = 0

while q:
    now_dist, now_node = heapq.heappop(q)

    if dist[now_node] < now_dist:
        continue

    for next_node, wgt in graph[now_node]:
        next_dist = now_dist + wgt

        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(q, [next_dist, next_node])


print(dist[n])
