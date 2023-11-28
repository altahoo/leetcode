# 164. Maximum Gap

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n, min_num, max_num = len(nums), min(nums), max(nums)
        if n <= 2 or max_num == min_num:
            return max_num - min_num
        
        buckets = collections.defaultdict(list)
        for num in nums:
            idx = n - 2 if num == max_num else (num - min_num) * (n - 1) // (max_num - min_num)
            buckets[idx].append(num)
        
        candidates = [[min(buckets[i]), max(buckets[i])] for i in range(n - 1) if buckets[i]]
        return max(y[0] - x[1] for x, y in zip(candidates, candidates[1:]))