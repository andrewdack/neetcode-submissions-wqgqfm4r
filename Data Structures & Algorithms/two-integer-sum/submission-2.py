class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        i, j = 0, 0

        for n in range(len(nums)):
            diff = target - nums[n]
            if (diff in seen):
                return [seen[diff], n]
            else:
                seen[nums[n]] = n
        
