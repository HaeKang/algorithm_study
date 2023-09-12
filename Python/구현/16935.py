# https://www.acmicpc.net/problem/16935

import sys
input = sys.stdin.readline


def print_ans(ans):
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")

        print("")

# 상하 반대
def rotate_1(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * col_len for _ in range(row_len)]

    # 행번호 = 행길이 - 행번호 - 1
    # 열번호 = 열번호
    for i in range(row_len):
        for j in range(col_len):
            ans[row_len - i - 1][j] = arr[i][j]

    return ans

# 좌우반대
def rotate_2(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * col_len for _ in range(row_len)]

    # 행번호 = 행번호
    # 열번호 = 열길이 - 열번호 - 1
    for i in range(row_len):
        for j in range(col_len):
            ans[i][col_len - j - 1] = arr[i][j]

    return ans

# 90도
def rotate_3(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * row_len for _ in range(col_len)]

    # ans = list(map(list, zip(*arr[::-1])))

    # 행번호 = 회전 전 열번호
    # 열번호 = 행 길이 - 회전 전 행번호 - 1
    for i in range(row_len):
        for j in range(col_len):
            ans[j][row_len - i - 1] = arr[i][j]

    return ans


# -90도
def rotate_4(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * row_len for _ in range(col_len)]

    # ans = list(map(list, zip(*arr)))[::-1]

    # 행번호 = 열 길이 - 열 번호 - 1
    # 열번호 = 행번호
    for i in range(row_len):
        for j in range(col_len):
            ans[col_len - j - 1][i] = arr[i][j]

    return ans


# 5번
def rotate_5(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * col_len for _ in range(row_len)]

    # 1 -> 2
    # 행 번호 = 행 번호
    # 열 번호 = 열 번호 + m//2
    for i in range(row_len // 2):
        for j in range(col_len // 2):
            ans[i][j + col_len//2] = arr[i][j]

    # 2 -> 3
    # 행 번호 = 행 번호 + n//2
    # 열 번호 = 열번호
    for i in range(row_len // 2):
        for j in range(col_len//2, col_len):
            ans[i + row_len//2][j] = arr[i][j]

    # 3 -> 4
    # 행번호 = 행번호
    # 열번호 = 열번호 - m//2
    for i in range(row_len//2, row_len):
        for j in range(col_len//2, col_len):
            ans[i][j - col_len//2] = arr[i][j]

    # 4 -> 1
    # 행번호 = 행번호 - n//2
    # 열번호 = 열번호
    for i in range(row_len//2, row_len):
        for j in range(col_len//2):
            ans[i - row_len//2][j] = arr[i][j]

    return ans

# 6번


def rotate_6(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    ans = [[0] * col_len for _ in range(row_len)]

    # 1 -> 4
    # 행번호 = 행번호 + n//2
    # 열번호 = 열번호
    for i in range(row_len // 2):
        for j in range(col_len//2):
            ans[i + row_len//2][j] = arr[i][j]

    # 4 -> 3
    # 행번호 = 행번호
    # 열번호 = 열번호 + m//2
    for i in range(row_len//2, row_len):
        for j in range(col_len//2):
            ans[i][j + col_len//2] = arr[i][j]

    # 3 -> 2
    # 행 번호 = 행 번호 - n//2
    # 열번호 = 열번호
    for i in range(row_len//2, row_len):
        for j in range(col_len//2, col_len):
            ans[i - row_len//2][j] = arr[i][j]

    # 2 -> 1
    # 행번호 = 행번호
    # 열번호 = 열번호 - m//2
    for i in range(row_len//2):
        for j in range(col_len//2, col_len):
            ans[i][j - col_len//2] = arr[i][j]

    return ans


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

r_lst = list(map(int, input().split()))

for r in r_lst:
    if r == 1:
        arr = rotate_1(arr)
    elif r == 2:
        arr = rotate_2(arr)
    elif r == 3:
        arr = rotate_3(arr)
    elif r == 4:
        arr = rotate_4(arr)
    elif r == 5:
        arr = rotate_5(arr)
    elif r == 6:
        arr = rotate_6(arr)

print_ans(arr)
