# https://leetcode.com/problems/reverse-integer

# 풀이1
class Solution:
    def reverse(self, x: int) -> int:
        MAX_ANS = 2**31 - 1
        MIN_ANS = -2**31
        
        if x >= 0:
            x = list(str(x))
            x.reverse()
            x = ''.join(x)
            x = int(x)

        else:
            x = list(str(x)[1:])
            x.reverse()
            x = ''.join(x)
            x = int(x) * -1
        
        if MIN_ANS <= x <= MAX_ANS:
            return x
        else:
            return 0


# 풀이2
class Solution:
    def reverse(self, x: int) -> int:
        MAX_ANS = 2**31 - 1
        MIN_ANS = -2**31
        
        if x >= 0:
            x = str(x)[::-1]
            x = int(x)

        else:
            x = str(x)[1:]
            x = x[::-1]
            x = int(x) * -1
        
        if MIN_ANS <= x <= MAX_ANS:
            return x
        else:
            return 0
