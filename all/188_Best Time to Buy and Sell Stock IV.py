# 188. Best Time to Buy and Sell Stock IV

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [0] * n
        for _ in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, n):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return dp[-1]


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        
        if k > n:
            diff = [prices[i] - prices[i - 1] for i in range(1, n)]
            return sum([profit for profit in diff if profit > 0])
        
        dp = [0] * n
        for _ in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, n):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return dp[-1]