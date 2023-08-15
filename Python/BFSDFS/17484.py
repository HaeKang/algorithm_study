'''
https://www.acmicpc.net/problem/17484
dfs 버전
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = [-1, 0, 1]
ans = 1e9

# 행, 열, 방향, r.c까지의 합, 방문여부


def dfs(r, c, dir, sum):
    global ans

    if r == n-1:
        ans = min(ans, sum)

    for k in range(0, 3):
        if k == dir:    # 이전과 같은 방향이면 넘어가기
            continue

        nr = r + 1
        nc = c + dirs[k]

        # 범위 체크
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        dfs(nr, nc, k, sum + arr[nr][nc])


for j in range(m):
    for k in range(3):
        sum = arr[0][j]
        dfs(0, j, k, sum)

print(ans)
