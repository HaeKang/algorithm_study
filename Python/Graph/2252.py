import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)  # 진입차수

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()

# 진입차수 0인 노드 q에 넣어줌
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

ans = []

# 위상정렬
for _ in range(n):
    node = q.popleft()
    ans.append(node)

    for i in graph[node]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

for answer in ans:
    print(answer, end=" ")
