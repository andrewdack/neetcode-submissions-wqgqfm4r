class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, lprodList, rprodList = [], [], []
        lprod, rprod = 1, 1

        for i in range(len(nums)):
            lprodList.append(lprod)
            lprod *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            rprodList.insert(0, rprod)
            rprod *= nums[i]
        
        print(lprodList)
        print()
        print(rprodList)
            


        return [p1 * p2 for p1, p2 in zip(lprodList, rprodList)]