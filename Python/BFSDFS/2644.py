# https://www.acmicpc.net/problem/2644
# bfs 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))

m = int(input())

edges = [[] for _ in range(n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

checked = [0 for _ in range(n  +1)]
ans = -1

q = deque()
q.append([target[0], 0])

while q:
    now_node, now_num = q.popleft()

    if now_node == target[1]:
        ans = now_num
        break

    for edge in edges[now_node]:
        if checked[edge] == 0:
            checked[edge] = 1
            q.append([edge, now_num + 1])

print(ans)
