from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())

graph = []
virus = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 숫자, x, y좌표, 시간 받음
            virus.append((graph[i][j], i, j, 0))

target_s, target_x, target_y = map(int, input().split())
target_x -= 1
target_y -= 1

virus.sort()
q = deque(virus)

while q:
    v_name, x, y, s = q.popleft()

    # s초인 경우
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v_name
                q.append((v_name, nx, ny, s+1))

print(graph[target_x][target_y])
