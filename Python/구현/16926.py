# https://www.acmicpc.net/problem/16926
"""
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28

28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]


# deque의 rotate 이용해서 -r만큼 해주면 됨
q = deque()

# 테두리의 개수는 min(n, m) // 2개
for i in range(min(N,M) // 2):
    q.clear()

    # 위
    for c in range(i, M-i):
        q.append(arr[i][c])

    # 오
    for r in range(i + 1, N - 1 - i):
        q.append(arr[r][M - 1 - i])

    # 아래
    for c in range(M - 1 - i, i - 1, -1):
        q.append(arr[N - 1 - i][c])

    # 왼
    for r in range(N - 1 - i - 1, i, -1):
        q.append(arr[r][i])

    q.rotate(R * -1)

    # 배열 복귀
    
    # 위
    for c in range(i, M-i):
        arr[i][c] = q.popleft()

    # 오
    for r in range(i + 1, N - 1 - i):
         arr[r][M - 1 - i] = q.popleft()

    # 아래
    for c in range(M - 1 - i, i - 1, -1):
        arr[N - 1 - i][c] = q.popleft()

    # 왼
    for r in range(N - 1 - i - 1, i, -1):
        arr[r][i] = q.popleft()

for n in range(N):
    print(" ".join(arr[n]))
