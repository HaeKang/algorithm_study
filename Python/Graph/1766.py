import sys
from queue import PriorityQueue

# 우선순위큐 + 위상정렬

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = PriorityQueue()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.put(i)


results = []

# 모든 문제를 풀어야 하므로 n만큼
for _ in range(n):
    node = q.get()
    results.append(node)

    for n in graph[node]:
        indegree[n] -= 1

        if indegree[n] == 0:
            q.put(n)


for ans in results:
    print(ans, end=" ")
