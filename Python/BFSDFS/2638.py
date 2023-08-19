'''
https://www.acmicpc.net/problem/2638
bfs
'''
from collections import deque

n, m = map(int, input().split())    # row, col

arr = [list(map(int, input().split())) for _ in range(n)]  # 치즈:1, 노치즈:0, 1이상 (치즈가 공기랑 맞닿은 수 (-1 해줘야함))

ans = 0

cheese_cnt = 0  # 치즈 수
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cheese_cnt += 1

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# bfs -> 바깥 공기만 bfs 돌도록, 치즈면 큐에 넣지 않는다
def bfs(r, c):
    global cheese_cnt

    q = deque()
    q.append([r, c])
    checked[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            # 범위체크
            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue

            if checked[next_r][next_c] == 0:
                if arr[next_r][next_c] >= 1:
                    arr[next_r][next_c] += 1
                else:
                    checked[next_r][next_c] = 1
                    q.append([next_r, next_c])


while cheese_cnt > 0:
    # print("남은 치즈 개수 : ", cheese_cnt)
    checked = [[0] * m for _ in range(n)]

    bfs(0, 0)

    # 치즈 없애기
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                cheese_cnt -= 1
                arr[i][j] = 0
            elif arr[i][j] >= 1:
                arr[i][j] = 1   # 원상복구

    ans += 1

print(ans)
