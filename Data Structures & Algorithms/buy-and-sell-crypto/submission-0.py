class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_prices = float("inf")

        for i in range(len(prices)):

            min_prices = min(min_prices , prices[i])
            max_profit = max(max_profit , prices[i] - min_prices)

        return max_profit



        

