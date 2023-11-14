# 123. Best Time to Buy and Sell Stock III

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # four states
        # buy 1st stock
        # sell 1st stock
        # buy 2nd stock
        # sell 2nd stock
        s1, s2, s3, s4 = -prices[0], float('-inf'), float('-inf'), float('-inf')
        for price in prices:
            s1 = max(s1, -price)
            s2 = max(s2, s1 + price)
            s3 = max(s3, s2 - price)
            s4 = max(s4, s3 + price)
        
        return max(s4, 0)