class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        maxS = nums[0]
        best = 0
        while i < len(nums):
            if best < 0:
                best = 0
            best += nums[i]
            maxS = max(maxS, best)
            i += 1
        return maxS