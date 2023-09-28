# https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        

        p_lst = [0] * n
        p_lst[start_node] = 1

        h = []
        heapq.heappush(h, [-1, start_node])

        while h:
            p, node = heapq.heappop(h)
            p *= -1

            if node == end_node:
                return p
            
            if p < p_lst[node]:
                continue
            
            for next_node, next_p in graph[node]:
                next_p = p * next_p

                if next_p > p_lst[next_node]:
                    p_lst[next_node] = next_p
                    heapq.heappush(h, [-next_p, next_node])
    
        return 0
