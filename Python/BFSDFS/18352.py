from collections import deque

# 백준 시간초과 해결
import sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]    # [0~n][0~n] size 2차원배열 선언
distance = [-1] * (n+1)  # 거리

distance[x] = 0  # 출발도시
q = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


q.append(x)

while q:
    node = q.popleft()

    for i in graph[node]:
        if distance[i] == -1:
            distance[i] = distance[node] + 1
            q.append(i)


flag = False

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True


if flag == False:
    print(-1)
