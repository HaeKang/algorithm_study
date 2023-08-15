'''
https://www.acmicpc.net/problem/17484
dp
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[1e9] * 3 for i in range(m)] for i in range(n)]
dir = [-1, 0, 1]    # 왼쪽 대각선, 아래, 오른쪽 대각선

for j in range(m):
    for k in range(3):
        dp[0][j][k] = arr[0][j]

for i in range(1, n):
    for j in range(m):
        for d in range(3):
            if (j == 0 and d == 0) or (j == m-1 and d == 2):
                dp[i][j][d] = 1e9
                continue

            if d == 0:
                dp[i][j][d] = min(
                    arr[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2]), dp[i][j][d])
            elif d == 1:
                dp[i][j][d] = min(
                    arr[i][j] + min(dp[i-1][j][0], dp[i-1][j][2]), dp[i][j][d])
            else:
                dp[i][j][d] = min(
                    arr[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1]), dp[i][j][d])


ans = 1e9
for j in range(m):
    ans = min(ans, min(dp[n-1][j]))
print(ans)
