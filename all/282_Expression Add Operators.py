# 282. Expression Add Operators

# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        output = []
        
        def dfs(i, equation, result, prev):
            if i >= n:
                if result == target:
                    output.append(''.join(equation))
                return
            
            for j in range(i, n):
                candidate = int(num[i: j+1])
                if not equation:
                    dfs(j + 1, [num[i: j + 1]], candidate, candidate)
                else:
                
                    dfs(j + 1, equation + ['+'] + [num[i: j + 1]], result + candidate, candidate)
                    dfs(j + 1, equation + ['-'] + [num[i: j + 1]], result - candidate, -candidate)
                    dfs(j + 1, equation + ['*'] + [num[i: j + 1]], result - prev + candidate * prev, candidate * prev)

                if num[i] == '0':
                    break
        
        dfs(0, [], 0, 0)
        return output

