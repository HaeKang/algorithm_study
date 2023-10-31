# https://leetcode.com/problems/interleaving-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        # dp[idx][0] : s1의 idx - 1 ~ idx번째 == s3의 idx - 1 ~ idx번째 => True, 다르면 False
        # dp[0][idx] : 위와 동일
        # dp[i][j] : s1의 i번째 문자와 s2의 j번째 문자를 통해 s3의 i + j 번째 문자와 동일하면 True
        dp[0][0] = True
        print(dp)

        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]
