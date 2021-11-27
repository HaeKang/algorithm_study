import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    lists = list(map(int, input().split()))
    for i in range(2, len(lists)):  # lists[0] 은 pd가 부를 가수의 수 이므로 제외
        graph[lists[i-1]].append(lists[i])
        indegree[lists[i]] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

results = []

while q:
    node = q.popleft()
    results.append(node)

    for i in graph[node]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

if len(results) != n:
    print("0")
else:
    for i in results:
        print(i)
