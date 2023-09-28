# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[1e9] * n for _ in range(n)]

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # 자기자신 거리 0
        for i in range(n):
            dist[i][i] = 0
        
        # 플로이드와샬
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = 1e9
        ans_cnt = 1e9
        for i in range(n):
            tmp_cnt = 0
            for d in dist[i]:
                if d <= distanceThreshold:
                    tmp_cnt += 1
            
            if tmp_cnt <= ans_cnt:
                ans = i
                ans_cnt = tmp_cnt

        return ans

