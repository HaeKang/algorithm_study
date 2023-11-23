# https://www.acmicpc.net/problem/2667
"""
1) 그래프 문제다
2) 가중치 없으니까 다익스트라, 크루스칼은 아닌듯
3) 최단거리 아니니까 dfs ㄱㄱ
"""

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
checked = [[0 for _ in range(n)] for _ in range(n)]

ans = []
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

cnt = 0


def dfs(r, c):
    global cnt

    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if checked[nr][nc] == 0 and arr[nr][nc] == '1':
            checked[nr][nc] = 1
            dfs(nr, nc)


for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and checked[i][j] == 0:
            cnt = 0
            checked[i][j] = 1
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
