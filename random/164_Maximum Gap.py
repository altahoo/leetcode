# 164. Maximum Gap

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n, nums_min, nums_max = len(nums), min(nums), max(nums)
        if n <= 2 or nums_min == nums_max:
            return nums_max - nums_min
        
        buckets = collections.defaultdict(list)
        for num in nums:
            idx = n - 2 if num == nums_max else (num - nums_min) * (n - 1)// (nums_max - nums_min)
            buckets[idx].append(num)
        
        candidates = [[min(buckets[i]), max(buckets[i])] for i in range(n - 1) if buckets[i]]
        return max(y[0] - x[1] for x, y in zip(candidates, candidates[1:]))