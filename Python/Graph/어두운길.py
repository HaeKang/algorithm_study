# 크루스칼

# 특정 원소가 포함된 집합 찾기 ~ 특정 원소의 root 찾기
def find_parent(parent, x):
    # 해당 원소가 root가 아니면 ~ root찾을때까지 반복
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 루트 노드 동일하게 -> 사이클 체크 위해
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n개의집 m개의 도로
n, m = map(int, input().split())

edges = []  # (거리, x집, y집)
ans = 0  # 최소비용

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

# 거리순으로 정렬 ~ 오름차순
edges.sort()

# 루트노드 저장
parents = [0] * (n+1)

# 루트를 자기 자신으로 설정
for i in range(1, n+1):
    parents[i] = i


total = 0  # 가로등 비용


# 크루스칼 시작

for e in edges:
    cost, a, b = e
    total += cost

    # 사이클이 발생하지 않는 경우
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        ans += cost


# 얼마나 아낄수 있냐
print(total - ans)
