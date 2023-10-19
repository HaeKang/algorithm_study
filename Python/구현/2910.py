# https://www.acmicpc.net/problem/2910

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

num_cnt = {} 
for idx in range(len(arr)):
    num = arr[idx]

    if num in num_cnt:
        num_cnt[num] = [num_cnt[num][0] + 1, num_cnt[num][1]]
    else:
        num_cnt[num] = [1, idx]

cnt_arr = []
for x, y in num_cnt.items():
    cnt_arr.append([y[0], y[1], x])

cnt_arr.sort(key = lambda x : (x[0] * -1, x[1]))

for idx in range(len(cnt_arr)):
    for _ in range(cnt_arr[idx][0]):
        print(cnt_arr[idx][2], end = " ")

