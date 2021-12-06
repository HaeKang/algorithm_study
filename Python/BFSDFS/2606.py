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
