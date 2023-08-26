'''
https://www.acmicpc.net/problem/1253
'''
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(n):
    tmp_arr = arr[:i] + arr[i+1:]

    start = 0
    end = len(tmp_arr) - 1

    while start < end:
        sum = tmp_arr[start] + tmp_arr[end]

        if sum == arr[i]:
            ans += 1
            break

        if sum < arr[i]:
            start += 1

        else:
            end -= 1

print(ans)
