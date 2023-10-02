# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1, n+1)]
arr = deque(arr)


while True:
    if len(arr) == 1:
        break

    # 맨 앞 버리기
    arr.popleft()

    # 아래로 옮기기
    target = arr.popleft()
    arr.append(target)

print(arr.popleft())

