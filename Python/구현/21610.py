import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
moves = []

# 8가지 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]


for _ in range(m):
    d, s = map(int, input().split())    # 구름 이동 방향, 거리
    moves.append([d - 1, s])

# 비 구름 위치
cloud = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]


for i in range(m):
    # 구름 이동
    move = moves[i]
    next_cloud = []  # 이동 후 구름 위치 저장

    for c in cloud:

        d = move[0]  # 방향
        s = move[1]  # 칸수
        x = c[0]
        y = c[1]

        nx = x + s * dx[d]
        ny = y + s * dy[d]

        # 범위수정
        if nx >= n:
            nx %= n
        elif nx < 0:
            nx = (n - 1) - (((-1) * nx - 1) % n)
        if ny >= n:
            ny %= n
        elif ny < 0:
            ny = (n - 1) - (((-1) * ny - 1) % n)

        next_cloud.append([nx, ny])

    # 물의 양 증가
    check = [[-1] * n for _ in range(n)]    # 5번조건때문에 만듬

    for c in next_cloud:
        x = c[0]
        y = c[1]

        arr[x][y] += 1
        check[x][y] = 1

    # 구름 리셋
    cloud = []

    # 물복사
    for c in next_cloud:
        cnt = 0     # 대각선에 물이 있는 구름 수

        x = c[0]
        y = c[1]

        for j in range(4):
            nx = x + dx2[j]
            ny = y + dy2[j]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 1:
                cnt += 1

        arr[x][y] += cnt

    # 물의 양 2 인 이상인 곳에 구름 생성 및 물 -2
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and check[i][j] == -1:
                arr[i][j] -= 2
                cloud.append([i, j])

ans = 0
for i in range(n):
    ans += sum(arr[i])

print(ans)
