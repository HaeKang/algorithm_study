# https://www.acmicpc.net/problem/2606

# dfs 풀이
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

answer = 0

com_cnt = int(input())
edge_cnt = int(input())

arr = [[] for _ in range(com_cnt + 1)]
checked = [0 for _ in range(com_cnt + 1)]

for _ in range(edge_cnt):
    c1, c2 = map(int, input().split())
    arr[c1].append(c2)
    arr[c2].append(c1)

def dfs(com):
    global answer


    for next_node in arr[com]:
        if checked[next_node] == 0:
            checked[next_node] = 1
            answer += 1
            dfs(next_node)

    return

checked[1] = 1
dfs(1)
print(answer)


# bfs 풀이
from collections import deque

# 컴퓨터 수
n = int(input())

graph = [[] for _ in range(n+1)]

# 0 : no visit, 1 : visit
visit = [0] * (n+1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
q.append(1)
visit[1] = 1

ans = 0

while q:
    node = q.popleft()

    for next_node in graph[node]:
        if visit[next_node] == 0:
            q.append(next_node)
            visit[next_node] = 1
            ans += 1

print(ans)
