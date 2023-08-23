# 309. Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy[i] = max(buy[i - 1], rest[i - 1] - price[i])
        # sell[i] = max(sell[i - 1], buy[i - 1] + price[i])
        # rest[i] = sell[i - 1]
        # buy[i] = max(buy[i - 1], sell[i - 2] - price[i])

        sell, buy = 0, -float(inf)
        pre_sell, pre_buy = 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)

        return sell