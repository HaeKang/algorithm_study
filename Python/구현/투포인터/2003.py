# https://www.acmicpc.net/problem/2003
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


start = 0
end = 1

ans = 0
while start <= end and end <= n:
    tmp_sum = sum(arr[start:end])

    if tmp_sum == m:
        ans += 1
        start += 1

    elif tmp_sum < m:
        end += 1

    else:
        start += 1

print(ans)
