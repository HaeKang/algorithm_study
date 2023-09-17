# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * 3 for _ in range(n)]

for _ in range(n):
    idx, gold, silver, bronze = map(int, input().split())

    arr[idx - 1][0] = gold
    arr[idx - 1][1] = silver
    arr[idx - 1][2] = bronze


# 금메달, 은메달, 동메달 기준 정렬
sort_arr = sorted(list(enumerate(arr)),
                  key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))

ranks = [0] * n

for i in range(n):
    if i == 0:
        ranks[sort_arr[i][0]] = i + 1

    if i > 0:
        if sort_arr[i][1] == sort_arr[i - 1][1]:
            ranks[sort_arr[i][0]] = ranks[sort_arr[i - 1][0]]
        else:
            ranks[sort_arr[i][0]] = i + 1

print(ranks[k - 1])
