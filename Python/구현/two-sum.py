# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            a = target - nums[i]

            if a in nums:
                a_idx = nums.index(a)
                if a_idx != i:
                    return [i, a_idx]
