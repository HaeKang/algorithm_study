'''
https://www.acmicpc.net/problem/1083
10
19 20 17 18 15 16 13 14 11 12
5

20 19 18 17 16 15 14 13 12 11
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())


for i in range(n):
    start = i   # 탐색 시점
    end = start + s + 1 # 최대로 소팅할 수 있는 거리

    if end >= n:
        end = n

    now_max = max(arr[start:end])
    now_max_idx = arr.index(now_max)
    
    # 현재 위치가 최대치면 패스
    if now_max_idx == start:
        continue

    s -= (now_max_idx - start)
    
    
    # 한칸씩 뒤로 밀기
    for j in range(now_max_idx, start, -1):
        arr[j-1], arr[j] = arr[j], arr[j-1]
    
    if s <= 0:
        break    

print(' '.join(map(str, arr)))
