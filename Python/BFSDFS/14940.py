'''
https://www.acmicpc.net/problem/14940
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())    # 행, 열

arr = [list(map(int, input().split())) for _ in range(n)]
checked = [[-1] * m for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(row, col):
    q = deque()
    q.append([row, col])
    checked[row][col] = 0

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue

            if checked[next_r][next_c] == -1 and arr[next_r][next_c] != 0:
                q.append([next_r, next_c])
                checked[next_r][next_c] = checked[now_r][now_c] + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=" ")
        else:
            print(checked[i][j], end=" ")

    print()
