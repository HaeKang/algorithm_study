# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    checked = [-1 for _ in range(n+1)]
    arr = [[] for _ in range(n+1)]
    
    for a, b in roads:
        arr[a].append(b)
        arr[b].append(a)
    
    q = deque()
    q.append(destination)
    checked[destination] = 0
    
    while q:
        node = q.popleft()
        
        for next in arr[node]:
            if checked[next] == -1:
                checked[next] = checked[node] + 1
                q.append(next)
    
    for i in sources:
        answer.append(checked[i])
        
    return answer
