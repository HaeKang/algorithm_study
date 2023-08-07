'''
https://leetcode.com/problems/find-eventual-safe-states/
위상정렬 활용
'''

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_graph = [[] for _ in range(len(graph))]
        indegrees = [0] * (len(graph))

        for i in range(len(graph)):
            for node in graph[i]:
                new_graph[node].append(i)
                indegrees[i] += 1


        q = deque()
        for i in range(len(graph)):
            if indegrees[i] == 0:
                q.append(i) 

        answer = []
        
        while q:
            now_node = q.popleft()
            answer.append(now_node)

            for next_node in new_graph[now_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    q.append(next_node)

        answer.sort()
        return answer
