# https://www.acmicpc.net/problem/2591

import sys
input = sys.stdin.readline

card = input().rstrip()

# i = card 인덱스, j : 0 (단독 사용), 1 (전의 숫자와 연결하여 2자리수로 사용)
dp = [[0, 0] for _ in range(len(card))]

dp[0][0] = 1
dp[0][1] = 0

for i in range(1, len(card)):
    # 2자리수로 사용하는 경우
    if 10 <= int(card[i-1] + card[i]) <= 34:
        dp[i][1] = dp[i-1][0]
      
    # 현재 숫자가 0이 아닌 경우만 단독으로 사용 가능
    if card[i] != '0':
        dp[i][0] = dp[i-1][0] + dp[i-1][1]

print(dp[len(card)-1][0] + dp[len(card)-1][1])
