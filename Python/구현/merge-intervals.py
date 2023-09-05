# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for arr in intervals:
            if len(ans) == 0:
                ans.append(arr)
            
            elif ans[-1][1] < arr[0]:
                ans.append(arr)
            
            else:
                ans[-1][1] = max(ans[-1][1], arr[1])
        
        return ans
