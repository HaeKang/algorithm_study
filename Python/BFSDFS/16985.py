'''
https://www.acmicpc.net/problem/16985
너무 어려웠던 문제.........

5개 순열 ~ permutations
최단거리 ~ bfs
시간초과 해결을 위해 exit() 활용

'''

import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

arr = [[list(map(int, input().split(' ')))
        for _ in range(5)] for _ in range(5)]
case_arr = [[[0] * 5 for _ in range(5)] for _ in range(5)]
ans = 1e9

dh = [0, 0, 0, 0, 1, -1]
dr = [0, 0, 1, -1, 0, 0]
dc = [1, -1, 0, 0, 0, 0]

# 최단거리 구하기
def bfs():
    global ans

    q = deque()
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    q.append((0, 0, 0))

    while q:
        h, r, c = q.popleft()

        if h == 4 and r == 4 and c == 4:
            ans = min(ans, dist[4][4][4])

            if ans == 12:
                print(ans)
                exit()
            return

        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if nh < 0 or nh >= 5 or nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue

            if case_arr[nh][nr][nc] == 0 or dist[nh][nr][nc] != 0:
                continue

            q.append((nh, nr, nc))
            dist[nh][nr][nc] = dist[h][r][c] + 1

# 배열 90도 회전
def rotate(rotate_arr):
    return list(map(list, zip(*rotate_arr[::-1])))

# 배열 회전 후 bfs 시작
def rotate_arr(cnt):
    if cnt == 5:
        if case_arr[4][4][4] == 1:
            bfs()
        return

    for _ in range(4):
        if case_arr[0][0][0]:   # 출발이 가능한 경우만 (첫 좌표가 1)
            rotate_arr(cnt + 1)

        case_arr[cnt] = rotate(case_arr[cnt])


# 5개의 판을 랜덤으로 쌓음
for p in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        case_arr[p[i]] = arr[i]

    rotate_arr(0)

if ans == 1e9:
    print(-1)
else:
    print(ans)
