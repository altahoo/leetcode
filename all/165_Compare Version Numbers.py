# 165. Compare Version Numbers

# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(val) for val in version1.split('.')]
        version2 = [int(val) for val in version2.split('.')]
        for val1, val2 in zip(version1, version2):
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        
        l1, l2 = len(version1), len(version2)
        if l1 > l2:
            # check version1[l2:]
            for val in version1[l2:]:
                if val:
                    return 1
        else:
            # check version2[l1:]
            for val in version2[l1:]:
                if val:
                    return -1
        return 0