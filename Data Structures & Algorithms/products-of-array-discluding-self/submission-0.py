class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if j != i:
                    p *= nums[j]
            res.append(p)
        return res