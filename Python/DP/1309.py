# https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

MOD = 9901

n = int(input())

# dp[i][j] 
# i = 행번호
# j = 0 (사자없음), 1 (왼쪽에 사자), 2 (오른쪽에 사자)
dp = [[0,0,0] for _ in range(n + 1)]


dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

# 점화식
for i in range(2, n+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2] 
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]

    for j in range(3):
        dp[i][j] %= MOD

print(sum(dp[n]) % MOD)
