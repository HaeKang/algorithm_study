import sys
from collections import deque

input = sys.stdin.readline

# 테스트케이스
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())    # 건물개수, 규칙

    graph = [[False] * (n+1) for i in range(n+1)]  # edge 간선 방향
    indegree = [0] * (n+1)  # 진입차수
    d = list(map(int, input().split()))  # 건설 시간

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = True  # x->y
        indegree[y] += 1  # y의 진입차수 +1

    w = int(input())    # 마지막점 ~ 마지막 건물번호

    q = deque()

    time_arr = [0] * (n+1)   # 시간 담아두기

    # 진입차수 0인 건물 q에 넣음
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            time_arr[i] = d[i - 1]

    # 위상정렬 시작
    for _ in range(n):
        node = q.popleft()

        # 최대값 찾기
        for i in range(1, n+1):
            if graph[i][node] == True:
                time_arr[node] = max(
                    time_arr[node], time_arr[i] + d[node-1])    # 현재 저장된 나의 값 / 나랑 연결된 값 + 내 건물짓는 시간

        if node == w:
            break

        for j in range(1, n+1):
            if graph[node][j] == True:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)
                    time_arr[j] = d[j-1]

    print(time_arr[w])
