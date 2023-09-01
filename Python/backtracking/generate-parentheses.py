# https://leetcode.com/problems/generate-parentheses/description/?envType=featured-list&envId=top-interview-questions%3FenvType%3Dfeatured-list&envId=top-interview-questions

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(lst, open_cnt, close_cnt):

            if close_cnt == n:
                ans.append(''.join(lst))
            
            if open_cnt < n:
                backtracking(lst + ["("], open_cnt + 1 , close_cnt)

            # ( 여는괄호 가 ) 닫는괄호 보다 더 많이 있으면 닫아주는 경우도 추가해주면 됨
            if close_cnt < open_cnt:
                backtracking(lst + [")"], open_cnt, close_cnt + 1)
        
        backtracking([], 0, 0)
        return ans
