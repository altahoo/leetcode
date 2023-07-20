# 189. Rotate Array
class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Solution 1: extra space O(n)
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Solution 2: extra space O(1)
        """
        def _swap(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        _swap(0, n - 1)
        _swap(0, k - 1)
        _swap(k, n - 1)