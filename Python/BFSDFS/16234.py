import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# bfs


def bfs(i, j):
    q = deque()
    q.append([i, j])
    check[i][j] = True

    union = []
    union.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == False:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    check[nx][ny] = True
                    q.append([nx, ny])
                    union.append([nx, ny])   # 연합 추가

    return union


ans = 0

while True:
    check = [[False] * n for _ in range(n)]
    isMove = False  # 인구이동여부

    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                union = bfs(i, j)

                if len(union) > 1:
                    isMove = True
                    num = sum(graph[x][y] for x, y in union) // len(union)
                    for x, y in union:
                        graph[x][y] = num

    if isMove == False:
        break

    ans += 1

print(ans)
