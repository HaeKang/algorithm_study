# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

6
"""

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
    ans += (k // arr[i])
    k = k % arr[i]

print(ans)
        
