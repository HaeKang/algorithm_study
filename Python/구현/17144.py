import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
robot_top = 0
robot_bottom = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 1초마다 미세먼지 확산


def spread():

    change = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                tmp = 0
                for i in range(4):
                    ax = x + dr[i]
                    ay = y + dc[i]
                    if 0 <= ax < r and 0 <= ay < c:
                        if board[ax][ay] != -1:
                            change[ax][ay] += board[x][y]//5
                            tmp += board[x][y]//5
                board[x][y] -= tmp
    for x in range(r):
        for y in range(c):
            board[x][y] += change[x][y]


def top_rotate():
    d = 1
    before = 0
    x, y = robot_top, 1
    while True:
        ax = x + dr[d]
        ay = y + dc[d]
        if ax == r or ay == c or ax == -1 or ay == -1:
            d = (d-1) % 4
            continue
        if x == robot_top and y == 0:
            break
        board[x][y], before = before, board[x][y]
        x, y = ax, ay


def bottom_rotate():
    d = 1
    before = 0
    x, y = robot_bottom, 1
    while True:
        ax = x + dr[d]
        ay = y + dc[d]
        if ax == r or ay == c or ax == -1 or ay == -1:
            d = (d+1) % 4
            continue
        if x == robot_bottom and y == 0:
            break
        board[x][y], before = before, board[x][y]
        x, y = ax, ay


for i in range(r):
    if board[i][0] == -1:
        robot_top = i
        robot_bottom = i+1
        break

for _ in range(t):
    spread()
    top_rotate()
    bottom_rotate()

answer = 2
for i in range(r):
    answer += sum(board[i])
print(answer)
