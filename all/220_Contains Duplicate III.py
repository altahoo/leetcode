# 220. Contains Duplicate III

# You are given an integer array nums and two integers indexDiff and valueDiff.

# Find a pair of indices (i, j) such that:

# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        size = valueDiff + 1
        for i, num in enumerate(nums):
            bucket_id = num // size
            if bucket_id in buckets:
                return True
            # Check neighbors
            for j in (bucket_id - 1, bucket_id + 1):
                if j in buckets:
                    if abs(buckets[j] - num) < size:
                        return True
            
            buckets[bucket_id] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // size]
        
        return False

