# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def _combination(start, cur_sum, cur_result):
            if start >= len(candidates) or cur_sum > target:
                return
            if cur_sum == target:
                result.append(cur_result.copy())
                return
            
            # Include candidates[start] in potential results
            cur_result.append(candidates[start])
            _combination(start, cur_sum + candidates[start], cur_result)
            cur_result.pop()
            # Exclude candidates[start] from potential results
            _combination(start + 1, cur_sum, cur_result)
        
        _combination(0, 0, []) 
        return result    