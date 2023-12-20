# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])
        
        for i in range(k, len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            queue.append(i)
            result.append(nums[queue[0]])
        return result
