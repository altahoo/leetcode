# 18. 4Sum

lass Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            first = nums[i]
            if i > 0 and nums[i - 1] == first:
                continue
            for j in range(i + 1, n):
                second = nums[j]
                if j > i + 1 and second == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = first + second + nums[left] + nums[right]
                    if total == target:
                        result.append([first, second, nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif total > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return result