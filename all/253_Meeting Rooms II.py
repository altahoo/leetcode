# 253. Meeting Rooms II

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0]) #sort by start time
        min_heap = [intervals[0][1]] #store the end times of the on-going meetings
        result = 1

        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heappop(min_heap)
            else:
                result += 1
            heappush(min_heap, end)
        return result
