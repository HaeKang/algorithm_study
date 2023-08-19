'''
https://www.acmicpc.net/problem/2636
bfs
'''
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

cheese_cnt = 0  # 전체 치즈 수
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:
            cheese_cnt += 1

ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0, 0])
    checked[0][0] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                continue

            if checked[next_r][next_c] == 0:
                if arr[next_r][next_c] >= 1:
                    arr[next_r][next_c] += 1
                else:
                    checked[next_r][next_c] = 1
                    q.append([next_r, next_c])


# print("처음 치즈 갯수 : ", cheese_cnt)
while cheese_cnt > 0:
    delete_cnt = 0    # 지운 치즈의 수

    checked = [[0] * c for _ in range(r)]
    bfs()

    for i in range(r):
        for j in range(c):
            if arr[i][j] >= 2:
                delete_cnt += 1
                cheese_cnt -= 1
                arr[i][j] = 0

    # print("지운 치즈 수 : ", delete_cnt)
    ans += 1

print(ans)
print(delete_cnt)
