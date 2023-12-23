# 248. Strobogrammatic Number III

# Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:

    def generateStrobogrammaticNumber(self, n):
        candidates = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        i = n % 2
        queue = ['0', '1', '8'] if i == 1 else ['']

        while i < n:
            i += 2
            next_level = []

            for num in queue:
                for key, value in candidates.items():
                    if not (i == n and key == '0'):
                        next_level.append(key + num + value)
            queue = next_level
        
        return queue

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        result = []
        for n in range(len(low), len(high) + 1):
            result += self.generateStrobogrammaticNumber(n)
        
        low, high = int(low), int(high)
        result = [i for i in result if low <= int(i) <= high]
        
        return len(result)
