# 60. Permutation Sequence

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        result = []
        factorial = math.factorial(n)
        index = k - 1

        while nums:
            factorial //= len(nums)
            pos = index // factorial
            number = nums.pop(pos)
            result.append(number)
            index %= factorial
        
        return ''.join(result)
