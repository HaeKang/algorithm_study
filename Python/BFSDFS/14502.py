# bfs 풀이
# https://www.acmicpc.net/problem/14502
# bfs + 조합
import sys
from collections import deque
input = sys.stdin.readline

# n : row, m : col
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ans = 0

# 처음 안전영역의 갯수
init_zero_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            init_zero_cnt += 1


def bfs_virus(): 

    checked = [[0] * m for _ in range(n)]
    append_virus_cnt = 0

    # 바이러스 확산 >> bfs
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
               q.append([i, j])
               checked[i][j] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < m and checked[next_r][next_c] == 0:
                if arr[next_r][next_c] == 0:
                    q.append([next_r, next_c])
                    checked[next_r][next_c] = 1
                    append_virus_cnt += 1
    
    global ans, init_zero_cnt
    # 바이러스 수, 벽 갯수 제외
    ans = max(ans, init_zero_cnt -  append_virus_cnt - 3)


# 벽 3개 세우기
def make_wall(count):
    if count == 3:
        bfs_virus()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(count + 1)
                arr[i][j] = 0


make_wall(0)
print(ans)

# dfs 풀이
import copy
from itertools import combinations

n, m = map(int, input().split())

# graph 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


# dfs 구현
def dfs(x, y):
    graph_[x][y] = 2

    for step in range(4):
        nx = x + dx[step]
        ny = y + dy[step]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        if graph_[nx][ny] != 0:
            continue
        else:
            dfs(nx, ny)


# virus, zeros 위치 저장
virus = []
zeros = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            zeros.append([i, j])

# 3개의 벽이 세워질 수 있는 경우의 수
zeros_combi = combinations(zeros, 3)

# 3개의 벽이 세워질 수 있는 경우의 수 마다 안전한 지역을 safety_zone_list에 저장
# for문이 끝나면 max(safety_zone_list) 통해 값 return
safety_zone_list = []
for combi in zeros_combi:
    graph_ = copy.deepcopy(graph)

    graph_[combi[0][0]][combi[0][1]] = 1
    graph_[combi[1][0]][combi[1][1]] = 1
    graph_[combi[2][0]][combi[2][1]] = 1

    for vi in virus:
        dfs(vi[0], vi[1])

    safety_zone = 0
    for row in range(n):
        for col in range(m):
            if graph_[row][col] == 0:
                safety_zone += 1

    safety_zone_list.append(safety_zone)

print(max(safety_zone_list))
