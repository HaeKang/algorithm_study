'''
https://www.acmicpc.net/problem/2589
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
8
'''
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


arr = [list(input()) for _ in range(r)]

ans = 0

def bfs(start_r, start_c):
    global ans

    checked = [[-1] * c for _ in range(r)]

    q = deque()
    q.append([start_r, start_c])
    checked[start_r][start_c] = 0

    while q:
        now_r, now_c = q.popleft()
        now_dist = checked[now_r][now_c]

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                continue

            if checked[next_r][next_c] == -1 and arr[next_r][next_c] == 'L':        
                q.append([next_r, next_c])
                checked[next_r][next_c] = now_dist + 1

    now_max = 0
    for data in checked:
        now_max = max(now_max,max(data))
    
    ans = max(ans, now_max)

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            bfs(i, j)

print(ans)
