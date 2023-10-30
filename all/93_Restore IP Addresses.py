# 93. Restore IP Addresses

# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.restore(s, 0, [], result)
        return result
    
    def restore(self, s, k, cur_result, result):
        if k == 4 and not s:
            result.append('.'.join(cur_result))
        
        def _isValid(substr):
            if not substr or len(substr) > 3 or (len(substr) > 1 and substr[0] == '0'):
                return False
            return 0 <= int(substr) <= 255
        
        for i in range(1, 4):
            if len(s) >= i and _isValid(s[:i]):
                cur_result.append(s[:i])
                self.restore(s[i:], k + 1, cur_result, result)
                cur_result.pop()