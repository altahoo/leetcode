# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        partial, total = 0, 0
        start = 0
        for i, (gas_i, cost_i) in enumerate(zip(gas, cost)):
            partial += gas_i - cost_i
            total += gas_i - cost_i
            if partial < 0:
                start = i + 1
                partial = 0
        if total >= 0:
            return start
        return -1