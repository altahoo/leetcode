# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start > result[-1][-1]:
                result.append([start, end])
                continue
            result[-1][1] = max(result[-1][1], end)
        
        return result