# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert = False
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                insert = True
                break
        
        if not insert:
            intervals += [newInterval]
        
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)
        return result