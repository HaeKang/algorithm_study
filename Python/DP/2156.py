# https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
dp = [0] * (n)

if n >= 3:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i], dp[i-1])

elif n == 2:
    dp[1] = arr[0] + arr[1]

else:
    dp[0] = arr[0]
    
print(max(dp))
