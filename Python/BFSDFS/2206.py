# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()

    # checked[r][c][0] 은 벽 파괴 가능, checked[r][c][1] 은 불가능
    checked = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    # r, c, 벽파괴여부
    q.append([0, 0, 0])
    checked[0][0][0] = 1

    while q:
        r, c, flag = q.popleft()

        if r == n - 1 and c == m - 1:
            return checked[r][c][flag]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if arr[nr][nc] == '1' and flag == 0:
                checked[nr][nc][1] = checked[r][c][flag] + 1
                q.append([nr, nc, 1])

            if arr[nr][nc] == '0' and checked[nr][nc][flag] == 0:
                checked[nr][nc][flag] = checked[r][c][flag] + 1
                q.append([nr, nc, flag])

    return -1


print(bfs())
