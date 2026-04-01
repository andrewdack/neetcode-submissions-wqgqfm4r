class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = len(nums) - 1
        canMake = False
        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]
            if val < target - i:
                canMake = False
            else:
                canMake = True
                target = i
        return canMake