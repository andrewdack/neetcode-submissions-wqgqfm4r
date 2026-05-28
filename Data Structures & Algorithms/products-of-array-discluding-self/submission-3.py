class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lprodList, rprodList = [0] * l, [0] * l
        lprod, rprod = 1, 1

        for i in range(len(nums)):
            lprodList[i] = lprod
            lprod *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            rprodList[i] = rprod
            rprod *= nums[i]

        return [p1 * p2 for p1, p2 in zip(lprodList, rprodList)]