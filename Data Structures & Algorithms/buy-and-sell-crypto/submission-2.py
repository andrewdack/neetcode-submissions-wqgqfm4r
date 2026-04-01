class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                m = max((prices[j] - prices[i]), m)
        return m