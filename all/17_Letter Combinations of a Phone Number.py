# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        result = set()

        def _generate(idx, substr):
            if len(substr) == len(digits):
                result.add(substr)
                return
            for letter in mapping[int(digits[idx])]:
                _generate(idx + 1, substr + letter)

        for i in range(len(digits)):
            _generate(0, '')
        
        return list(result)