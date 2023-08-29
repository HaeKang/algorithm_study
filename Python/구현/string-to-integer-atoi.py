"""
https://leetcode.com/problems/string-to-integer-atoi
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_ANS = 2**31 - 1
        MIN_ANS = -2**31

        s = s.strip()

        if len(s) == 0:
            return 0
        
        flag = 1

        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        ans = []

        for data in s:
            if data.isdigit():
                ans.append(data)
            else:
                break
        if len(ans) == 0:
            return 0
        
        else:
            ans = ''.join(ans)
            ans = int(ans)
            ans = flag * ans

            if ans <= MIN_ANS:
                return MIN_ANS
            elif ans >= MAX_ANS:
                return MAX_ANS
            else:
                return ans
