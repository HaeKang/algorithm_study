from collections import deque


def bfs(start_node):
    visit = [start_node]
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in range(len(arr[start_node])):
            if(arr[node][i] == 1 and (i not in visit)):
                visit.append(i)
                queue.append(i)


def dfs(node, visit=[]):
    visit.append(node)
    print(node, end=' ')

    for i in range(len(arr[node])):
        if(arr[node][i] == 1 and (i not in visit)):
            dfs(i, visit)


n, m, v = map(int, input().split())
arr = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    arr[n1][n2] = arr[n2][n1] = 1

dfs(v)
print()
bfs(v)
