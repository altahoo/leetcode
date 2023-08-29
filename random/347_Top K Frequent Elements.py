# 347. Top K Frequent Elements

import collections, heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result