# 215. Kth Largest Element in an Array

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
        return heapq.heappop(heap)