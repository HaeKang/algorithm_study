# 크루스칼

# 시간초과로 인해 sys.stdin.readline 이용
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 -> root 노드 동일시하기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n개의 행성
n = int(input())

x = []  # (위치, 행성번호)
y = []
z = []
edges = []  # (거리)(행성번호)(행성번호)
ans = 0

for i in range(1, n+1):
    x1, y1, z1 = map(int, input().split())
    x.append((x1, i))
    y.append((y1, i))
    z.append((z1, i))

x.sort()
y.sort()
z.sort()


for i in range(n-1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정

    # (거리)(행성번호)(행성번호)
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()


# 루트노드 저장
parents = [0] * (n+1)

# 루트를 자기 자신으로 설정
for i in range(1, n+1):
    parents[i] = i


# 간선을 하나씩 확인하며
for e in edges:
    cost, a, b = e
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        ans += cost

print(ans)
