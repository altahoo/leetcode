# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        max_len = 0
        for num in nums:
            if num in visited:
                continue
            length = 1
            visited.add(num)
            cur = num - 1
            while cur in nums:
                length += 1
                visited.add(cur)
                cur -= 1
                
            cur = num + 1
            while cur in nums:
                length += 1
                visited.add(cur)
                cur += 1
            
            max_len = max(max_len, length)
        
        return max_len
