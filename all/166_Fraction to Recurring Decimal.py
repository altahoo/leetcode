# 166. Fraction to Recurring Decimal

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        result = ''
        n, d = abs(numerator), abs(denominator)
        result += str(n // d)
        remainder = n % d

        if remainder:
            result += '.'
            remainder_idx = {}
            while remainder:
                if remainder in remainder_idx:
                    idx = remainder_idx[remainder]
                    result = result[:idx] + '(' + result[idx:] + ')'
                    break
                
                remainder_idx[remainder] = len(result)
                remainder *= 10
                result += str(remainder // d)
                remainder %= d

        return result if numerator * denominator > 0 else '-' + result