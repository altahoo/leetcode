# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        def _combination(cur_result, cur_idx):
            cur_sum = sum(cur_result)
            if cur_sum == target:
                result.append(cur_result.copy())
                return

            if cur_sum > target:
                return
            
            idx = cur_idx
            while idx < len(candidates):
                if candidates[idx] > target:
                    break
                cur_result.append(candidates[idx])
                _combination(cur_result, idx + 1)
                cur_result.pop()
                idx += 1
                while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                    idx += 1
        
        _combination([], 0)

        return result
