# https://www.acmicpc.net/problem/2573
"""
4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0
1
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global n, m

    remove_ice_lst = []

    q = deque()
    checked[r][c] = 1
    q.append([r, c])

    while q:
        now_r, now_c = q.popleft()
        remove_cnt = 0

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue

            if arr[next_r][next_c] == 0:
                remove_cnt += 1

            if checked[next_r][next_c] == 0 and arr[next_r][next_c] > 0:
                checked[next_r][next_c] = 1
                q.append([next_r, next_c])

        if remove_cnt > 0:
            remove_ice_lst.append([now_r, now_c, remove_cnt])

    for r, c, cnt in remove_ice_lst:
        arr[r][c] = max(0, arr[r][c] - cnt)


time = 0
group_flag = True     # 분리여부

while group_flag:
    checked = [[0] * m for _ in range(n)]
    group = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and checked[i][j] == 0:
                group += 1
                bfs(i, j)

    if group == 0:
        break
    elif group > 1:
        group_flag = False
        break

    time += 1

if group_flag == False:
    print(time)
else:
    print(0)
