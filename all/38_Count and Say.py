# 38. Count and Say

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"

        for i in range(2, n + 1):
            curr = []
            cur_num = ''
            cur_cnt = 0
            for j in range(len(prev)):
                cur_num = prev[j]
                if j == 0 or cur_num == prev[j - 1]:
                    cur_cnt += 1
                    continue
                curr.append((cur_cnt, prev[j - 1]))
                cur_cnt = 1
            curr.append((cur_cnt, cur_num))   
            prev = ''.join([str(cur_cnt) + str(cur_num) for (cur_cnt, cur_num) in curr])
        
        return prev