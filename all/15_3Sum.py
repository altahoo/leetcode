# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return result
        
        for i, num in enumerate(nums):
            if num > 0:
                return result
            if i > 0 and num == nums[i - 1]:
                continue
            target = -num
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -num:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1  
                elif  nums[left] + nums[right] > -num:
                    right -= 1
                else:
                    left += 1
        return result