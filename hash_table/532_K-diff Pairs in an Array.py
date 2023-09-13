# 532. K-diff Pairs in an Array

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        result = set()
        for num in nums:
            if counter[num] <= 0:
                continue
            counter[num] -= 1
            if counter[num + k] > 0:
                result.add((num, num + k))
            if k != 0 and counter[num - k] > 0:
                result.add((num - k, num))
        return len(result)