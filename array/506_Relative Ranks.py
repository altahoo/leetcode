# 506. Relative Ranks

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [-num for num in score]
        heapq.heapify(heap)

        num_rank = {}
        for i in range(len(score)):
            num = heapq.heappop(heap)
            if i == 0:
                num_rank[-num] = 'Gold Medal'
            elif i == 1:
                num_rank[-num] = 'Silver Medal'
            elif i == 2:
                num_rank[-num] = 'Bronze Medal'
            else:
                num_rank[-num] = f'{i + 1}'
        
        result = []
        for _, num in enumerate(score):
            result.append(num_rank[num])
        
        return result