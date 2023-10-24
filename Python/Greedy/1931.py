# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4
"""

n = int(input())

arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

# 1. 끝나는 시간을 key로 sort
arr.sort(key = lambda x : (x[1], x[0]))

ans = 0
last_end = 0   # 회의실 시작 가능 시간
for i in range(n):
    now_start = arr[i][0]
    now_end = arr[i][1]

    # 현재 idx의 회의가 시작 가능하면
    # 처음에 = 안써서 틀림. 끝난 시간에 시작이 가능하므로 = 붙여줘야함
    if now_start >= last_end:
        last_end = now_end
        ans += 1
    
print(ans)
