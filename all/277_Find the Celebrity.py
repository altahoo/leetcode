# 277. Find the Celebrity

# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set([i for i in range(n)])
        i = 0
        while len(candidates) > 1:
            for j in range(i + 1, n):
                i_knows_j = knows(i, j)
                if i_knows_j:
                    if i in candidates:
                        candidates.remove(i)
                elif j in candidates:
                    candidates.remove(j)
            i += 1
        
        if not candidates:
            return -1

        candidate = list(candidates)[0]
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate