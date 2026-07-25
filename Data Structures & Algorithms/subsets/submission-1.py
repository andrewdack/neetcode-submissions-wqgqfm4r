class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        def search(i, curSubset):
            if i == n:
                res.append(curSubset.copy())
                return

            search(i + 1, curSubset)
            curSubset.append(nums[i])
            
            search(i + 1, curSubset)
            curSubset.pop()
    
                  
        
        search(0, [])
        return res

        