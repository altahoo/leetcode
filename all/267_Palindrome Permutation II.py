# 267. Palindrome Permutation II

# Given a string s, return all the palindromic permutations (without duplicates) of it.

# You may return the answer in any order. If s has no palindromic permutation, return an empty list.

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def can_palindrom(s):
            s_counter = collections.Counter(s)
            odd = ''
            for letter, count in s_counter.items():
                if count % 2 == 0:
                    continue
                if not odd:
                    odd = letter
                else:
                    return None, None
            return s_counter, odd
        
        
        def generate_candidates(s_counter, odd):
            candidates = []
            for letter, count in s_counter.items():
                if letter == odd:
                    count -= 1
                candidates += [letter] * (count // 2)
            return candidates
        
        def permute(nums):
            permutations = set()
            n = len(nums)

            def _permute(start):
                if start == n - 1:
                    permutations.add(tuple(nums.copy()))
                    return
                for i in range(start, n):
                    nums[start], nums[i] = nums[i], nums[start]
                    _permute(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

            _permute(0)
            return permutations

        s_counter, odd = can_palindrom(s)
        if not s_counter:
            return []
        
        if len(s_counter) == 1:
            return [s]
        
        candidates = generate_candidates(s_counter, odd)
        permutations = permute(candidates)

        result = []
        for permutation in permutations:
            result.append(''.join(permutation) + odd + ''.join(permutation[::-1]))
        return result