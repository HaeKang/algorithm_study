t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (30) for _ in range(30)]

    for i in range(30):  # 서쪽
        for j in range(30):  # 동쪽
            if i == 1:
                dp[i][j] = j
            if i == j:
                dp[i][j] = 1

            if i > j:
                dp[i][j] = 0

            if i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(dp[n][m])
