# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        i = n - 1
        while i >= 0:
            if i == n - 1:
                total = digits[i] + 1
            else:
                total = (digits[i] + carry)
            digits[i] = total % 10
            carry = total // 10
            i -= 1
            if carry == 0:
                break
        if carry:
            digits = [carry] + digits
        return digits