# https://www.acmicpc.net/problem/12100
# 백트래킹?
"""
4
2 16 16 0
32 16 4 1
4 16 32 0
2 0 8 8

128

"""

import sys
import copy
input = sys.stdin.readline

n = int(input())
ori_arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 최대값 구하기
def get_max(ans_arr):
    tmp = 0
    for i in range(len(ans_arr)):
        tmp = max(tmp, max(ans_arr[i]))
    return tmp


def move_left(arr):
    for r in range(n):
        merge_col = 0  # merge target col 인덱스
        for c in range(1, n):
            if arr[r][c] != 0:
                tmp = arr[r][c]
                arr[r][c] = 0

                # target col이 비어있는 경우 대체
                if arr[r][merge_col] == 0:
                    arr[r][merge_col] = tmp

                # 같은 값인 경우
                elif arr[r][merge_col] == tmp:
                    arr[r][merge_col] *= 2
                    merge_col += 1

                # 다른 값인 경우
                else:
                    merge_col += 1
                    arr[r][merge_col] = tmp

    return arr


def move_right(arr):
    for r in range(n):
        merge_col = n - 1
        for c in range(n - 2, -1, -1):
            if arr[r][c] != 0:
                tmp = arr[r][c]
                arr[r][c] = 0

                if arr[r][merge_col] == 0:
                    arr[r][merge_col] = tmp

                elif arr[r][merge_col] == tmp:
                    arr[r][merge_col] *= 2
                    merge_col -= 1

                else:
                    merge_col -= 1
                    arr[r][merge_col] = tmp
    return arr


def move_down(arr):
    for c in range(n):
        merge_row = n - 1
        for r in range(n - 1, -1, -1):
            if arr[r][c] != 0:
                tmp = arr[r][c]
                arr[r][c] = 0

                if arr[merge_row][c] == 0:
                    arr[merge_row][c] = tmp

                elif arr[merge_row][c] == tmp:
                    arr[merge_row][c] *= 2
                    merge_row -= 1

                else:
                    merge_row -= 1
                    arr[merge_row][c] = tmp

    return arr


def move_up(arr):
    for c in range(n):
        merge_row = 0
        for r in range(n):
            if arr[r][c] != 0:
                tmp = arr[r][c]
                arr[r][c] = 0

                if arr[merge_row][c] == 0:
                    arr[merge_row][c] = tmp

                elif arr[merge_row][c] == tmp:
                    arr[merge_row][c] *= 2
                    merge_row += 1

                else:
                    merge_row += 1
                    arr[merge_row][c] = tmp

    return arr


def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print("")


def backtracking(arr, cnt):
    global ans

    if cnt == 5:
        now_max = get_max(arr)
        if ans < now_max:
            ans = now_max
        return

    tmp_arr = copy.deepcopy(arr)
    backtracking(move_left(tmp_arr), cnt + 1)
    tmp_arr = copy.deepcopy(arr)
    backtracking(move_right(tmp_arr), cnt + 1)
    tmp_arr = copy.deepcopy(arr)
    backtracking(move_down(tmp_arr), cnt + 1)
    tmp_arr = copy.deepcopy(arr)
    backtracking(move_up(tmp_arr), cnt + 1)


backtracking(ori_arr, 0)
print(ans)
