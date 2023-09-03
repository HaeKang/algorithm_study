# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    answer = 0
    
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][len(triangle[i-1]) - 1] + triangle[i][j]
            
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]        
    
    answer = max(dp[-1])
    
    return answer
