from collections import deque
import sys

# 시간초과 방지
input = sys.stdin.readline

# n개의 과목 m개의 조건
n, m = map(int, input().split())

graph = [[False] * (n+1) for i in range(n+1)]
indegree = [0] * (n+1)  # 진입차수

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    indegree[b] += 1

# 위상정렬 시작
q = deque()

for i in range(n+1):
    if indegree[i] == 0:
        q.append([i, 1])    # 노드번호, 학기 수

# 답 [노드번호, 학기 수]
result = []

for i in range(n+1):

    now = q.popleft()
    node = now[0]
    cnt = now[1]

    result.append((node, cnt))

    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for j in range(1, n + 1):
        if graph[node][j]:
            indegree[j] -= 1

            if indegree[j] == 0:
                q.append([j, cnt+1])


# 노드순으로 sort
result.sort()

for i in range(1, n+1):
    print(result[i][1], end=' ')
