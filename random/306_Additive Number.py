# 306. Additive Number

# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            s1 = num[:i]   
            if len(s1) > 1 and s1[0] == '0':
                break
            for j in range(i + 1, len(num)):
                d1 = int(s1)
                s2 = num[i: j]
                if len(s2) > 1 and s2[0] == '0':
                    break
                d2 = int(s2)
                next_d = d1 + d2
                next_str = str(d1 + d2)
                if next_str != num[j: j + len(next_str)]:
                    continue
                all_str = s1 + s2 + next_str
                while len(all_str) < len(num):
                    d1 = d2
                    d2 = next_d
                    next_d = d1 + d2
                    next_str = str(next_d)
                    all_str += next_str
                if all_str == num:
                    return True
        return False


# Follow up: How would you handle overflow for very large input integers?
# Instead of using int(), create a function to "add" two strings