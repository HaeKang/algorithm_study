# https://www.acmicpc.net/problem/15683
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cctv_mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 2, 3], [0, 1, 2], [1, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

cctv = []   # cctv 번호, 행, 열
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([arr[i][j], i, j])

ans = 1e9


def dfs(cnt, dfs_arr):
    global ans

    if cnt == len(cctv):
        # 사각지대
        tmp = 0

        for i in range(n):
            for j in range(m):
                if dfs_arr[i][j] == 0:
                    tmp += 1

        ans = min(ans, tmp)
        return

    tmp_arr = copy.deepcopy(dfs_arr)

    now_cctv, now_r, now_c = cctv[cnt]
    for modes in cctv_mode[now_cctv]:
        for mode in modes:
            next_r = now_r
            next_c = now_c
            while True:
                next_r += dr[mode]
                next_c += dc[mode]

                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                    break

                if tmp_arr[next_r][next_c] == 6:
                    break

                if tmp_arr[next_r][next_c] == 0:
                    tmp_arr[next_r][next_c] = -1

        dfs(cnt + 1, tmp_arr)
        tmp_arr = copy.deepcopy(dfs_arr)


dfs(0, arr)
print(ans)
