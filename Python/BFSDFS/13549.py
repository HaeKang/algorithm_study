import sys
from collections import deque

n, k = map(int, input().split())
check = [-1] * 100001

q = deque()
q.append(n)
check[n] = 0

while q:
    node = q.popleft()
    #print(node, " ", check[node])

    if node == k:
        print(check[k])
        break

    # 처음에 틀린 이유 ~ 2배하는 case를 맨 뒤로 놔서
    if 0 <= node * 2 <= 100000:
        if check[node*2] == -1:
            q.append(node * 2)
            check[node*2] = check[node]

    if 0 <= node-1 <= 100000:
        if check[node-1] == -1:
            q.append(node-1)
            check[node-1] = check[node] + 1

    if 0 <= node+1 <= 100000:
        if check[node+1] == -1:
            q.append(node+1)
            check[node+1] = check[node] + 1
