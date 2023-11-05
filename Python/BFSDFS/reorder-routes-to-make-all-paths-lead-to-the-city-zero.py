# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dict = defaultdict(list)
        
        for a, b in connections:
            dict[a].append([b, 1])
            dict[b].append([a, 0])

        
        def dfs(location, parent):
            ans = 0

            for c, d in dict[location]:
                if c == parent:
                    continue
                
                ans += d + dfs(c, location)

            return ans
        
        return dfs(0, -1)
