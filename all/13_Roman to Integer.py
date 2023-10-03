# 13. Roman to Integer

lass Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        for i in range(len(s)):
            val = mapping[s[i]]
            if i == len(s) - 1 or mapping[s[i + 1]] <= val:
                result += val
            else:
                result -= val
        return result