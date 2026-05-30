class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell = 0, 1
        minBuyIndex = 0
        maxProfit = 0
        while sell < n:
            profit = prices[sell] - prices[buy] 

            if prices[sell] < prices[minBuyIndex]:
                minBuyIndex = sell
                buy = minBuyIndex
            
            sell += 1
            maxProfit = max(maxProfit, profit)

        # cant be negative
        return maxProfit