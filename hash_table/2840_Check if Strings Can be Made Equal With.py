# 2840. Check if Strings Can be Made Equal With Operations II

# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

# You can apply the following operation on any of the two strings any number of times:

# Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        m1_even, m1_odd, m2_even, m2_odd = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                m1_even[ch1] += 1
                m2_even[ch2] += 1
            else:
                m1_odd[ch1] += 1
                m2_odd[ch2] += 1
        
        return m1_even == m2_even and m1_odd == m2_odd
                