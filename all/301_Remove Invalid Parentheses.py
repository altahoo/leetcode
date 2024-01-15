# 301. Remove Invalid Parentheses

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        visited = set([s])
        queue = collections.deque([s])
        found = False
        
        while queue:
            t = queue.popleft()
            if self.isValid(t):
                result.append(t)
                found = True
            if found:
                continue
            for i in range(len(t)):
                if t[i] not in ['(', ')']:
                    continue
                string = t[:i] + t[i + 1:]
                if string not in visited:
                    queue.append(string)
                    visited.add(string)
        
        return result if result else ['']