# 29. Divide Two Integers

class Solution:  # TLE

    def _get_result(self, result, negative):
        result = result if not negative else -result
        if result > 2**31 - 1:
            result = 2 ** 31 - 1
        elif result < -2 ** 31:
            result = -2 ** 31
        return result

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        negative = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return self._get_result(dividend, negative)

        total = 0
        result = 0
        while total < dividend:
            result += 1
            total += divisor
        
        if total > dividend:
            result -= 1
        
        return self._get_result(result, negative)


# Bit manipulation
# divisor << i : divisor multiply 2 ** i
# 1 << i : 2 ** i
class Solution:

    def _get_result(self, result, negative):
        result = result if not negative else -result
        if result > 2**31 - 1:
            result = 2 ** 31 - 1
        elif result < -2 ** 31:
            result = -2 ** 31
        return result

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        negative = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        for i in range(31, -1, -1):
            if divisor << i <= dividend:  # if divisor multiplied by 2**i is <= dividend
                dividend -= divisor << i
                result += 1 << i
        
        return self._get_result(result, negative)