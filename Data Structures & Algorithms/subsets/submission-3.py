class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        def search(i, curSubset):
            if i == n:
                res.append(curSubset.copy())
                return

            curSubset.append(nums[i])
            search(i + 1, curSubset)
            
            curSubset.pop()
            search(i + 1, curSubset)
    
                  
        
        search(0, [])
        return res

        