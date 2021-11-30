import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]

dp[1][1] = arr[0][0]

for x in range(1, n+1):
    for y in range(1, m+1):
        dp[x][y] = arr[x-1][y-1] + dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]


k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1 - 1][y1-1])
    print(ans)
