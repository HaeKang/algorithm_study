'''
https://www.acmicpc.net/problem/2531
'''
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = []    # 회전 초밥

for _ in range(n):
    arr.append(int(input()))

ans = 0


for i in range(n):
    start = i
    end = start + k

    if end < n:
        select = arr[start:end] + [c]

    else:
        select = arr[start:] + arr[:(end - n)] + [c]

    select = set(select)
    ans = max(ans, len(select))

print(ans)
