# 324. Wiggle Sort II

# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time: O(nlgn)
        Space: O(n)
        """
        tmp = sorted(nums, reverse=True)
        n = len(nums)
        mid = n // 2
        first = mid
        second = 0
        for i in range(n):
            if i % 2 == 1:
                nums[i] = tmp[second]
                second += 1
            else:
                nums[i] = tmp[first]
                first += 1


class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # code from: 215. Kth Largest Element in an Array
        # modified from kth largest -> kth smallest
        start, end = 0, len(nums) - 1
        while True:
            i, j = start, end
            pivot = nums[end]
            while i < j:
                if nums[i] > pivot:
                    while j > i and nums[j] > pivot:
                        j -= 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            if nums[j] > pivot:
                j -= 1
            if j == k:
                return pivot
            if j < k:
                start = j
                while start < k and nums[start] <= pivot:
                    start += 1
            else:
                end = j
                while end > k and nums[end] == pivot:
                    end -= 1

    def wiggleSort(self, nums: List[int]) -> None:
        # get the median. avg O(n) time and constant space
        median = self.findKthSmallest(nums, len(nums) // 2)

        idx_less, idx_greater = 0, 1
        # swap elements to the correct list (even or odd index)
        # this whole process is O(n) because each element moves at most once
        for idx in range(0, len(nums), 2): # even idx. swap until the element <= median
            while nums[idx] > median:
                nums[idx], nums[idx_greater] = nums[idx_greater], nums[idx]
                idx_greater += 2
        for idx in range(idx_greater, len(nums), 2): # odd idx
            while nums[idx] < median:
                nums[idx], nums[idx_less] = nums[idx_less], nums[idx]
                idx_less += 2

        # move all medians on the even list to the left
        i, j = 0, len(nums) - 1
        if j & 1:
            j -= 1  # make sure j is even
        while j > 0 and nums[j] != median:
            j -= 2  # find the last non-median elelment

        while i < j:
            if nums[i] == median:
                i += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 2

        # move all medians on the odd list to the right
        i, j = 1, len(nums) - 1
        if (j & 1) == 0:
            j -= 1  # make sure j is odd
        while i < j and nums[i] != median:
            i += 2  # find the first non-median element

        while i < j:
            if nums[j] == median:
                j -= 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2