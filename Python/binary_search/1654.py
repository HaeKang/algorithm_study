# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
ans = []

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for a in arr:
        cnt += (a // mid)

    if cnt >= n:
        ans.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(ans))
