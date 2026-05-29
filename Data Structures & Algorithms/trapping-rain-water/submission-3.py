class Solution:
    def trap(self, height: List[int]) -> int:
        lHeights = [-1] * len(height)
        rHeights = [-1] * len(height)

        peak = False
        for i in range(len(height)):
            if i == 0 and height[i] > 0:
                peak = True
            elif i == 0:
                continue
            elif peak and height[i - 1] > height[i]:
                lHeights[i] = height[i - 1]
                peak = False
            elif lHeights[i - 1] > height[i]:
                lHeights[i] = lHeights[i - 1]
            elif height[i] >= lHeights[i - 1]:
                peak = True


        peak = False
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1 and height[i] > 0:
                peak = True
            elif i == len(height) - 1:
                continue
            elif peak and height[i + 1] > height[i]:
                rHeights[i] = height[i + 1]
                peak = False
            elif rHeights[i + 1] > height[i]:
                rHeights[i] = rHeights[i + 1]
            elif height[i] >= rHeights[i + 1]:
                peak = True
        
        print(lHeights)
        print()
        print(rHeights)

        water = 0
        # last iteration
        for i in range(len(height)):
            minH = min(lHeights[i], rHeights[i])
            if minH == -1:
                continue
            water += minH - height[i]
        return water
            

        