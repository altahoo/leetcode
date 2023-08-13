# 912. Sort an Array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        num_count = collections.Counter(nums)
        result = []
        for num in range(-50000, 50001):
            if num_count[num] > 0:
                for _ in range(num_count[num]):
                    result.append(num)
        return result
