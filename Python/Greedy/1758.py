# https://www.acmicpc.net/problem/1758
"""
많은 금액을 받으면 좋으므로, money 정렬 후 
큰 돈이 1등에 가깝도록 함
처음에 음수처리 안해서 틀림..
"""
import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

ans = 0
for idx, money in enumerate(arr, start = 1):
    money = (money - (idx - 1))
    if money > 0:
        ans += money

print(ans)
