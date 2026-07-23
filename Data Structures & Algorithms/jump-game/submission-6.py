class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        reqDest = len(nums) - 1
        canMake = False

        i = reqDest - 1
        while i >= 0:
            mJLen = nums[i]

            #check if you can make the jump
            if (reqDest - i) <= mJLen:
                reqDest = i
                if i == 0:
                    canMake = True
            i -= 1
        
        return canMake


