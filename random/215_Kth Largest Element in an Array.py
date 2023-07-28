# 215. Kth Largest Element in an Array

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k > 0:
            result = heapq.heappop(max_heap)
            k -= 1
        return -result