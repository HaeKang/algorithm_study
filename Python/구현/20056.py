import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

# board 해당 칸에 존재하는 파이어볼 정보 저장
board = [[deque() for _ in range(n)] for _ in range(n)]

fireball = deque()

# 8가지 방향 (x:row, y:col)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for i in range(m):
    # row,col, 질량, 속력, 방향
    r, c, m, s, d = map(int, input().split())

    fireball.append([r-1, c-1])
    board[r-1][c-1].append(deque([m, s, d]))


# k번 이동 시작
for _ in range(k):
    for _ in range(len(fireball)):
        r, c = fireball.popleft()
        m, s, d = board[r][c].popleft()

        nr = (r + s * dx[d]) % n
        nc = (c + s * dy[d]) % n

        # 파이어볼 이동 정보 넣음
        board[nr][nc].append(deque([m, s, d]))

    for i in range(n):
        for j in range(n):
            # 파이어볼이 두개 이상
            if len(board[i][j]) > 1:
                # 질량 합, 속력 합, 개수, 홀수, 짝수
                sum_m = 0
                sum_s = 0
                fireball_cnt = 0
                odd_cnt = 0
                even_cnt = 0

                # board[i][j]에 있는 파이어볼 개수 만큼 while문
                while board[i][j]:
                    m, s, d = board[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    fireball_cnt += 1

                    # 방향 짝홀
                    if d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1

                sum_m = sum_m // 5
                sum_s = sum_s // fireball_cnt

                # 질량 0 파이어볼 소멸
                if sum_m == 0:
                    continue

                next_d = []

                if even_cnt == fireball_cnt or odd_cnt == fireball_cnt:
                    next_d = [0, 2, 4, 6]
                else:
                    next_d = [1, 3, 5, 7]

                # 파이어볼 합쳐서 4개로 나눈 정보 넣음
                for dir in next_d:
                    fireball.append([i, j])
                    board[i][j].append([sum_m, sum_s, dir])

            # 파이어볼이 한개
            elif len(board[i][j]) == 1:
                fireball.append([i, j])

ans = 0
for i in range(n):
    for j in range(n):
        if len(board[i][j]) > 0:
            for m, s, d in board[i][j]:
                ans += m

print(ans)
