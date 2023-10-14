# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                multi = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = multi + result[p2]
                result[p1] += total // 10
                result[p2] = total % 10
        
        result = ''.join([str(i) for i in result]).lstrip('0')
        return result