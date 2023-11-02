# https://leetcode.com/problems/word-search/submissions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # m : row, n = col
        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c, k):
            
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            
            if board[r][c] != word[k]:
                return False    
            
            tmp = board[r][c]
            board[r][c] = "-"
            
            res = False
            for i in range(4):
                if dfs(r + dr[i], c + dc[i], k + 1):
                    res = True
                    break
        
            board[r][c] = tmp

            return res
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
