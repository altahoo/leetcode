# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        return (self.findKth(nums1, nums2, (m + n + 1) // 2) + self.findKth(nums1, nums2, (m + n + 2) // 2)) / 2.0

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        i = min(len(nums1), k // 2)
        j = min(len(nums2), k // 2)
        if nums1[i - 1] > nums2[j - 1]:
            return self.findKth(nums1, nums2[j:], k - j)
        return self.findKth(nums1[i:], nums2, k - i)