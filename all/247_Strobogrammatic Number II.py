# 247. Strobogrammatic Number II

# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidates = {
            '0': '0',
            '1': '1',
            '6': '9', 
            '8': '8',
            '9': '6'
        }

        i = n % 2 # when n is even, start with 0; when n is odd, start with 1

        queue = ['0', '1', '8'] if i == 1 else ['']

        while i < n:
            i += 2
            next_level = []

            for num in queue:
                for key, val in candidates.items():
                    if not (i == n and key == '0'):
                        next_level.append(key + num + val)
            queue = next_level
        
        return queue