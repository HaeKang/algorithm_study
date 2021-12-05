import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 0

    if i == 2:
        dp[i] = 1

    if i == 3:
        dp[i] = 0

    if i-3 > 0:
        if(dp[i-3] == 0):
            dp[i] = 1
        else:
            dp[i] = 0

# 상근 = 0, 창영 = 1
if dp[n] == 0:
    print("SK")
else:
    print("CY")
