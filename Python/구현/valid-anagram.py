# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        for data in s:
            if s.count(data) != t.count(data):
                return False

        return True
