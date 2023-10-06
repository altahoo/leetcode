# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def _generate(tmp, left, right):
            if left == n:
                tmp += (n - right) * ')'
                result.append(tmp)
                return
            _generate(tmp + '(', left + 1, right)
            if left > right:
                _generate(tmp + ')', left, right + 1)

        _generate('', 0, 0)
        return result