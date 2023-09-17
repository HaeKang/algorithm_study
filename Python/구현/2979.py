# https://www.acmicpc.net/problem/2979

import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())

cars = [0] * 101
max_end = 0

for _ in range(3):
    s, e = map(int, input().split())
    max_end = max(max_end, e)

    for i in range(s, e):
        cars[i] += 1

ans = 0
for i in range(1, max_end):
    if cars[i] == 1:
        ans += a
    elif cars[i] == 2:
        ans += b * 2
    elif cars[i] == 3:
        ans += c * 3

print(ans)
