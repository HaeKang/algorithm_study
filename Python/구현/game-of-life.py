# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)  # row
        n = len(board[0])   # col

        for i in range(m):
            for j in range(n):

                live = 0

                for r in range(max(i - 1, 0), min(i + 2, m)):
                    for c in range(max(j - 1, 0), min(j + 2, n)):

                        if i == r and j == c:
                            continue
                        
                        live += board[r][c] % 2

                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                
                elif live < 2 or live > 3:
                    board[i][j] = 3
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1

                elif board[i][j] == 3:
                    board[i][j] = 0        
