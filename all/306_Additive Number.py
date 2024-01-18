# 306. Additive Number

# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            first = num[:i]
            if len(first) > 1 and first[0] == '0':
                continue

            for j in range(i + 1, n):
                num1 = int(first)
                second = num[i: j]
                if len(second) > 1 and second[0] == '0':
                    continue
                num2 = int(second)

                num_sum = num1 + num2
                str_sum = str(num_sum)
                if str_sum != num[j:j+len(str_sum)]:
                    continue
                
                solution = first + second + str_sum
                while len(solution) < n:
                    num1 = num2
                    num2 = num_sum
                    num_sum = num1 + num2
                    str_sum = str(num_sum)
                    solution += str_sum
                
                if solution == num:
                    return True
        return False