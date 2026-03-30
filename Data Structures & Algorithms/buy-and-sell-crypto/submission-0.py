class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        for i, num in enumerate(prices):
            for j in range(i+1, len(prices)):
                profit = prices[j] - num
                if profit > max_profit:
                    max_profit = profit
        return 0 if max_profit < 0 else max_profit