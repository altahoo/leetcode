# 278. First Bad Version

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            mid = start + (end - start) // 2
            curr_bad = isBadVersion(mid)
            prev_bad = isBadVersion(mid - 1) if mid > 0 else False
            if curr_bad and not prev_bad:
                return mid
            
            if not curr_bad:
                start = mid + 1
            else:
                end = mid - 1
        return start