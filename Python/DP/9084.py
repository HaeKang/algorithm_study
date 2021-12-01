import sys

input = sys.stdin.readline

# 테스트케이스
t = int(input())

max = 10001

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, target+1):
            if (i-coin) >= 0:
                dp[i] += dp[i-coin]

    print(dp[target])
