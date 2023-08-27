
'''
https://www.acmicpc.net/problem/1912
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [i for i in arr]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])


print(max(dp))
