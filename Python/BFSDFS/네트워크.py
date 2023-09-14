# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# dfs 풀이법
def dfs(i, n, checked, computers):
    for idx in range(n):
        if computers[i][idx] == 1 and checked[idx] == 0:
            checked[idx] = 1
            dfs(idx, n, checked, computers)


def solution(n, computers):
    answer = 0

    checked = [0] * (n)  # 방문여부

    for i in range(n):
        if checked[i] == 0:
            checked[i] = 1
            dfs(i, n, checked, computers)
            answer += 1

    return answer



# find-union 풀이법
def find_parent(i, parent):
    if parent[i] == i:
        return i
    else:
        return find_parent(parent[i], parent)


def union_parent(i, j, parent):
    parent_i = find_parent(i, parent)
    parent_j = find_parent(j, parent)

    if parent_i <= parent_j:
        parent[parent_j] = parent_i
    else:
        parent[parent_i] = parent_j


def solution(n, computers):
    answer = 0

    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if computers[i][j] == 1:
                union_parent(i, j, parent)
    # tc 9 반례
    # 5, [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
    answer = set()
    for i in range(n):
        answer.add(find_parent(i, parent))

    return len(answer)
