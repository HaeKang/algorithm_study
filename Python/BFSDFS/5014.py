# https://www.acmicpc.net/problem/5014
# 처음에 방문처리 안해서 틀림,,,
import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
checked = [0 for _ in range(f + 1)]

if s == g:
    print(0)
else:
    q = deque()
    q.append([s, 0])
    checked[s] = 1

    ans = 0

    while q:
        now_floor, now_cnt = q.popleft()

        if now_floor == g:
            ans = now_cnt
            break
        
        if now_floor + u <= f and u > 0:
            if checked[now_floor + u] == 0:
                checked[now_floor + u] = 1
                q.append([now_floor + u, now_cnt + 1])

        if now_floor - d >= 1 and d > 0:
            if checked[now_floor - d] == 0:
                checked[now_floor - d] = 1
                q.append([now_floor - d, now_cnt + 1])
    

    if ans == 0:
        print("use the stairs")
    else:
        print(ans)
