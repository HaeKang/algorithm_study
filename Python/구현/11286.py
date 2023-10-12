# https://www.acmicpc.net/problem/11286
import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(h, [abs(x), x])

    else:
        if len(h) > 0:
            target = heapq.heappop(h)
            print(target[1])
        else:
            print(0)
