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


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        result = 0
        for num, count in counter.items():
            if k == 0 and count > 1:
                result += 1
            elif k > 0 and counter[num + k] > 0:
                result += 1
        return result