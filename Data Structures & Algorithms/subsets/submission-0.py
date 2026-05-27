class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(index, path):
            if index == len(nums):
                results.append(path[:])
                return

            # case one, include num
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # case two, don't include num
            backtrack(index + 1, path)

        backtrack(0, [])

        return results