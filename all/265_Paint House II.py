# 265. Paint House II

# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n_houses = len(costs)
        if n_houses == 0:
            return 0
        n_colors = len(costs[0])

        for house in range(1, n_houses):
            for color in range(n_colors):
                min_cost = float('inf')
                for prev_color in range(n_colors):
                    if color != prev_color:
                        min_cost = min(min_cost, costs[house - 1][prev_color])
                costs[house][color] += min_cost

        return min(costs[-1])  