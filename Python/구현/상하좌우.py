n = int(input())
move = list(input().split())

x, y = 1, 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for m in move:
    if m == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
    elif m == 'L':
        nx = x + dx[1]
        ny = y + dy[1]
    elif m == 'D':
        nx = x + dx[2]
        ny = y + dy[2]
    elif m == 'U':
        nx = x + dx[3]
        ny = y + dy[3]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(nx, ny)
