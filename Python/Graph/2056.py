import sys
from collections import deque


input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
dp = [0] * (n+1)
indegree = [0] * (n+1)  # 진입차수

for i in range(1, n+1):
    lists = list(map(int, input().split()))  # 시간, 선행개수, 선행번호리스트
    times[i] = lists[0]
    dp[i] = lists[0]

    if lists[1] == 0:
        continue

    for j in range(lists[1]):
        start = i
        prev = lists[2+j]

        graph[prev].append(start)
        indegree[start] += 1    # 진입차수 1 상승

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)


while q:
    node = q.popleft()

    for i in graph[node]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[node] + times[i])

        if indegree[i] == 0:
            q.append(i)

print(max(dp))
