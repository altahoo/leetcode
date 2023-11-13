# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = []
        cur_min = float('inf')
        for price in prices:
            cur_min = min(cur_min, price)
            min_prices.append(cur_min)
         
        return max([(price - min_price) for price, min_price in zip(prices, min_prices)])
