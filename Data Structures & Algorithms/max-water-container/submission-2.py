class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer solution?
        # cur, next
        i = 0
        j = len(heights) - 1
        
        m = 0

        while i < j:
            if min(heights[i], heights[j]) * (j - i) > m:
                m = min(heights[i], heights[j]) * (j - i) 
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return m
            