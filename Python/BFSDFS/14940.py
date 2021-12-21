import sys
from collections import deque

input = sys.stdin.readline

# row, col
n, m = map(int, input().split())

# 0 : 갈수없음, 1 : 갈수있음, 2 : 목표지점
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[-1] * (m) for _ in range(n)]  # -1 : 미방문

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# bfs


def bfs(start_x, start_y):
    q = deque()

    q.append([start_x, start_y])
    check[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위체크 & 방문체크
            if (0 <= nx < n and 0 <= ny < m) and check[nx][ny] == -1 and arr[nx][ny] == 1:
                check[nx][ny] = check[x][y] + 1
                q.append([nx, ny])


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            check[i][j] = 0
        print(check[i][j], end=" ")
    print()
