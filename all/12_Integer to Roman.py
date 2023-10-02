# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        # 可以分为四类，100 到 300 一类，400 一类，500 到 800 一类，900 最后一类
        mapping = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
        result = ''

        for i, (unit, letter) in enumerate(mapping):
            if i % 2:
                continue
            digit = num // unit
            if digit < 4:
                result += digit * letter
            elif digit == 4:
                result += letter + mapping[i - 1][1]
            elif digit < 9:
                result += mapping[i - 1][1] + (digit - 5) * letter
            elif digit == 9:
                result += letter + mapping[i - 2][1]
            num %= unit

        return result