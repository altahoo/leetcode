# 767. Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = []
        for letter, cnt in counter.items():
            if cnt > (len(s) + 1) // 2:
                return ''
            heap.append((-cnt, letter))
        heapq.heapify(heap)

        result = []
        while len(heap) > 1:
            t1 = heapq.heappop(heap)
            t2 = heapq.heappop(heap)
            result.append(t1[1])
            result.append(t2[1])

            if t1[0] + 1 < 0:
                heapq.heappush(heap, (t1[0] + 1, t1[1]))
            if t2[0] + 1 < 0:
                heapq.heappush(heap, (t2[0] + 1, t2[1]))
        
        if heap:
            result.append(heap[0][1])
        return ''.join(result)
