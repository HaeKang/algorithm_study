# https://leetcode.com/problems/island-perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row_len = len(grid)
        col_len = len(grid[0])

        ans = 0

        for i in range(row_len):
            for j in range(col_len):
                # island
                if grid[i][j] == 1:

                    if j == 0 or grid[i][j-1] == 0:
                        ans += 1
                    
                    if i == 0 or grid[i-1][j] == 0:
                        ans += 1
                    
                    if i == row_len - 1 or grid[i+1][j] == 0:
                        ans += 1
                    
                    if j == col_len - 1 or grid[i][j+1] == 0:
                        ans += 1
        return ans
