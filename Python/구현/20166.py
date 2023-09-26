# https://www.acmicpc.net/problem/20166

import sys
input = sys.stdin.readline

# n : row, m : col
n, m, k = map(int, input().split())


dr = [0, 0, -1, 1, 1, -1, -1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

arr = [list(input().rstrip()) for _ in range(n)]

dict = {}   # key : word, value : 횟수

def dfs(r, c, cnt, result_str):
    if cnt > 5:
        return

    # 문자 나온 횟수 추가
    if result_str in dict:
        dict[result_str] = dict[result_str] + 1
    else:
        dict[result_str] = 1
    
    for i in range(8):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if next_r < 0:
            next_r = n -1
        
        if next_r >= n:
            next_r = 0
        
        if next_c < 0:
            next_c = m - 1

        if next_c >= m:
            next_c = 0

        dfs(next_r, next_c, cnt + 1, result_str + arr[next_r][next_c])

for i in range(n):
    for j in range(m):
        dfs(i, j, 1, arr[i][j])

while k:
    target = input().rstrip()

    if len(target) > 5 or len(target) == 0:
        print(0)
        k -= 1
        continue

    if target in dict:
        print(dict[target])
    else:
        print(0)

    k -= 1
