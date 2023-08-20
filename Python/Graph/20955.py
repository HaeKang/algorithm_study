'''
https://www.acmicpc.net/problem/20955
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])

    return x


def union_parnet(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
for _ in range(m):
    u, v = map(int, input().split())

    # cycle 체크
    if find_parent(u) == find_parent(v):
        ans += 1
    else:
        union_parnet(u, v)

for i in range(1, n):
    if find_parent(i) != find_parent(i+1):
        union_parnet(i, i+1)
        ans += 1

print(ans)
