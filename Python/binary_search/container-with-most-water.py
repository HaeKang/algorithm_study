# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        ans = 0

        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])  # 직사각형 영역 크기

            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return ans
