# 228. Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        nums += [float('inf')]
        result = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                # close the previous range
                if nums[i - 1] != result[-1][0]:
                    result[-1].append(nums[i - 1])
                # start a new range
                result.append([nums[i]])

        return [(str(r[0]) + '->' + str(r[1])) if len(r) == 2 else str(r[0]) for r in result[:-1]]