# https://www.acmicpc.net/problem/11508
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

ans = 0

for i in range(n // 3):
    start_idx = i * 3
    if start_idx < 0:
        start_idx = 0

    ans += arr[start_idx]
    ans += arr[start_idx + 1]

for i in range(1, n % 3 + 1):
    ans += arr[-1 * i]

print(ans)
