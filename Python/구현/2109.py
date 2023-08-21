'''
https://www.acmicpc.net/problem/2109

5
3 3
2 3
1 3
100 4
90 4

맞는 답 : 195

'''
import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1]))  # 날짜 기준 정렬

hq = []
for pay, day in arr:
    heapq.heappush(hq, pay)

    if len(hq) > day:
        heapq.heappop(hq)

print(sum(hq))
