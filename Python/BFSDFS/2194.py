'''
https://www.acmicpc.net/problem/2194
최단거리 ~> bfs
시작점 끝점 모두 제일 왼쪽상단 점을 주기에 이를 기준으로 풂
처음에 arr의 범위를 행,열 반대로 해줘서 틀렸다 주의하자
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m, a, b, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]   # 0 : 평지, -1 : 장애물, 1 이상 : 방문 및 출발지에서 거기까지의 거리

# 장애물 위치
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = -1

# 시작점, 끝점
start_row, start_col = map(int, input().split())
end_row, end_col = map(int, input().split())
start_row -= 1
start_col -= 1
end_row -= 1
end_col -= 1

# 범위 체크 (4개 모서리)
def check_range(r, c):
    global n, m, a, b, start_row, start_col

    # 시점
    if r == start_row and c == start_col:
        return False

    # 왼쪽 위
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    # 왼쪽 아래
    if (r + a - 1) < 0 or (r + a - 1) >= n or c < 0 or c >= m:
        return False

    # 오른쪽 위
    if r < 0 or r >= n or (c + b - 1) < 0 or (c + b - 1) >= m:
        return False
    
    # 오른쪽 아래
    if (r + a - 1) < 0 or (r + a - 1) >= n or (c + b - 1) < 0 or (c + b - 1) >= m:
        return False

    return True

# 장애물 체크
def check_error(r, c):
    global a, b

    for nr in range(r, r + a):
        for nc in range(c, c + b):
            if arr[nr][nc] == -1:
                return False

    return True

# bfs 시작
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
q = deque()
flag = False

q.append((start_row, start_col))

while q:
    now_row, now_col = q.popleft()

    if now_row == end_row and now_col == end_col:
        flag = True
        break

    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        # 범위 체크
        if check_range(next_row, next_col):
            # 장애물 체크
            if check_error(next_row, next_col):
                # 방문체크
                if arr[next_row][next_col] == 0:
                    arr[next_row][next_col] = arr[now_row][now_col] + 1
                    q.append((next_row, next_col))


if flag == False:
    print(-1)
else:
    print(arr[end_row][end_col])
