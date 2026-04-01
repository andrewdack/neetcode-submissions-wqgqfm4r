class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        
        water = 0
        while r > l:
            h1, h2 = heights[l], heights[r]
            w = min(h1, h2) * (r - l)
            water = max(water, w)
            if h1 < h2:
                l += 1
            else:
                r -= 1
        return water

            