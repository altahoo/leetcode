# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            a_val = int(a[i]) if i >= 0 else 0
            b_val = int(b[j]) if j >= 0 else 0
            total = a_val + b_val + carry
            carry = total // 2
            result.append(str(total % 2))
            i -= 1
            j -= 1
        
        if carry:
            result.append(str(carry))
        
        return ''.join(result[::-1])