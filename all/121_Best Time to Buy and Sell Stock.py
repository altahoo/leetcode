# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
         
        return profit
