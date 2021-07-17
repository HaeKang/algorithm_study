import sys
sys.setrecursionlimit(10**8)

n = int(input())
arr = [list(map(str, input())) for i in range(n)]
check1 = [[0]*n for i in range(n)]
check2 = [[0]*n for i in range(n)]
ans1 = 0
ans2 = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    check1[y][x] = 1
    color = arr[y][x]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n and 0 <= ny < n):
            if check1[ny][nx] == 0 and arr[ny][nx] == arr[y][x]:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if check1[j][i] == 0:
            dfs(i, j)
            ans1 += 1


def dfs2(x, y):
    check2[y][x] = 1
    color = arr[y][x]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n and 0 <= ny < n):
            if check2[ny][nx] == 0:
                n_color = arr[ny][nx]
                if(color == n_color):
                    dfs2(nx, ny)
                else:
                    if(color == 'G' and n_color == 'R'):
                        dfs2(nx, ny)
                    elif(color == 'R' and n_color == 'G'):
                        dfs2(nx, ny)


for i in range(n):
    for j in range(n):
        if check2[j][i] == 0:
            dfs2(i, j)
            ans2 += 1

print(ans1, ans2)
