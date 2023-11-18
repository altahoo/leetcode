# 134. Gas Station

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        partial, total = 0, 0
        start = -1
        for i, (cur_gas, cur_cost) in enumerate(zip(gas, cost)):
            partial += cur_gas - cur_cost
            total += cur_gas - cur_cost
            if partial < 0:
                start = i + 1
                partial = 0
        return start if total >= 0 else -1