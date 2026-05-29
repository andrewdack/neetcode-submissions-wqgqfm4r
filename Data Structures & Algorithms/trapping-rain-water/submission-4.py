class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        lh = [0] * n
        rh = [0] * n 
 
        lh[0] = height[0]
        for i in range(1, n):
            lh[i] = max(lh[i - 1], height[i])
        
        rh[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rh[i] = max(rh[i + 1], height[i])

        water = 0
        # last iteration
        for i in range(n):
            water += min(lh[i], rh[i]) - height[i]
        return water
            

        