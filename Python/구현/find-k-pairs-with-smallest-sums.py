# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        if len(nums1) == 0 or len(nums2) == 0:
            return ans
        
        h = []
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
        

        while k > 0 and h:
            s, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
            
            k -= 1
        
        return ans 
