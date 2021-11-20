# 위상정렬

from collections import deque

# 테스트 케이스
t = int(input())

for tc in range(t):
    # n개의 팀 (노드)
    n = int(input())

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    # [a 팀][b 팀] = True(a > b), F(b > a)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    # 작년 순위 정보 입력
    # idx : 등수, value : 팀번호
    data = list(map(int, input().split()))

    # 방향 그래프의 간선 정보 초기화 (작년기준)
    # 자기보다 낮은 등수의 팀을 가리키도록 edge 설정
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 순위 변경된 쌍의 수
    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())

        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []

    # queue보다 deque가 속도가 더 빠름 -> 코테에선 deque 사용 권장
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 한개인지 판단
    cycle = False  # 사이클이 존재 여부

    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break

        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    # 사이클 발생
    if cycle:
        print("IMPOSSIBLE")

    # 위상 정렬 결과가 여러 개
    elif not certain:
        print("?")

    else:
        for i in result:
            print(i, end=' ')
        print()
