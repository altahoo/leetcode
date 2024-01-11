# 291. Word Pattern II

# A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(cur, pattern, mappings):
            if not pattern:
                return not cur
            
            if pattern[0] in mappings:
                if cur[:len(mappings[pattern[0]])] != mappings[pattern[0]]:
                    return False
                return helper(cur[len(mappings[pattern[0]]):], pattern[1:], mappings)
            
            for i in range(len(cur)):
                if cur[:i+1] in mappings.values():
                    continue
                mappings[pattern[0]] = cur[:i + 1]
                if helper(cur[i + 1:], pattern[1:], mappings):
                    return True
                del mappings[pattern[0]]
            return False

        return helper(s, pattern, {})