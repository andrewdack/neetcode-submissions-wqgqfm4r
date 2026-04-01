class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        m = len(nums) // 2
        r = len(nums) - 1

        while l <= r:
            item = nums[m]
            if (target == item):
                return m
            if (target < item):
                r = m - 1
            if (target > item):
                l = m + 1  
            m = (r + l) // 2
        
        return -1