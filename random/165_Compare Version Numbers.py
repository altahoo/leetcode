# 165. Compare Version Numbers
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_1 = [int(i) for i in version1.split('.')]
        list_2 = [int(i) for i in version2.split('.')]
        n1, n2 = len(list_1), len(list_2)
        for i in range(min(n1, n2)):
            if list_1[i] < list_2[i]:
                return -1
            elif list_1[i] > list_2[i]:
                return 1
        if n1 == n2:
            return 0
        if n1 < n2:
            remaining = set(list_2[n1:])
            if remaining == {0}:
                return 0
            return -1
        remaining = set(list_1[n2:])
        if remaining == {0}:
            return 0
        return 1