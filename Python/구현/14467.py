import sys

input = sys.stdin.readline

# 관찰 횟수
n = int(input())

arr = [-1] * 11

ans = 0

for _ in range(n):
    num, location = map(int, input().split())

    if arr[num] == -1:
        arr[num] = location

    else:
        if arr[num] != location:
            ans += 1
            arr[num] = location

print(ans)
