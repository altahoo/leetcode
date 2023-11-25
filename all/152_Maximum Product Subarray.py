# 152. Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max, dp_min = [nums[0]], [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp_max.append(max(nums[i], nums[i] * dp_max[i - 1]))
                dp_min.append(min(nums[i], nums[i] * dp_min[i - 1]))
            else:
                dp_max.append(max(nums[i], nums[i] * dp_min[i - 1]))
                dp_min.append(min(nums[i], nums[i] * dp_max[i - 1]))
        return max(dp_max)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, result = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            tmp = cur_max
            if nums[i] > 0:
                cur_max = max(nums[i], nums[i] * cur_max)
                cur_min = min(nums[i], nums[i] * cur_min)
            else:
                cur_max = max(nums[i], nums[i] * cur_min)
                cur_min = min(nums[i], nums[i] * tmp)
            result = max(result, cur_max)
        return result


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, result = nums[0], nums[0], nums[0]
        
        for num in nums[1:]:
            tmp = cur_max
            cur_max = max(num, tmp * num, cur_min * num)
            cur_min = min(num, tmp * num, cur_min * num)
            result = max(result, cur_max)
        return result
