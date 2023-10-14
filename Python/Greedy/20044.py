# https://www.acmicpc.net/problem/20044
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = []

for i in range(0, n, 1):
    result.append(arr[i] + arr[(2 * n) - 1 - i])

print(min(result))
