class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                g = heights[i]
                if heights[i] > heights[j]:
                    g = heights[j]

                cur = g * (j - i)
                if (cur > maximum):
                    maximum = cur

        return maximum 