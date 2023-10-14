# https://www.acmicpc.net/problem/2012
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

ans = 0

arr.sort()

now_rank = 1
for a in arr:
    ans += (abs(a-now_rank))
    now_rank += 1

print(ans)
