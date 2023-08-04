66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i]
            digits[i] = int((tmp + carry) % 10)
            carry = int((tmp + carry) / 10)
            if carry == 0:
                break
        return [carry] + digits if carry else digits