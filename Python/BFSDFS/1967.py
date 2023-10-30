# https://www.acmicpc.net/problem/1967
"""
트리의 지름
x 에서 가장 먼 정점 y 를 구함
y 에서 가장 먼 정점 z 를 구함
y-z 의 거리가 트리의 지름
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

edges = [[] for _ in range(n+1)]
for _ in range(n - 1):
    root, child, cost = map(int, input().split())
    edges[root].append([child, cost])
    edges[child].append([root, cost])


def dfs(node, cost):
    for next in edges[node]:
        next_node = next[0]
        next_cost = next[1]

        if dist[next_node] == -1:
            dist[next_node] = cost + next_cost
            dfs(next_node, cost + next_cost)

# x 노드 : 1
dist = [-1 for _ in range(n+1)]
dist[1] = 0
dfs(1, 0)

# y 노드
new_node = 1
for i in range(1, n + 1):
    if dist[i] == max(dist):
        new_node = i
        break

# z 노드 구함
dist = [-1 for _ in range(n+1)]
dist[new_node] = 0
dfs(new_node, 0)
print(max(dist))
