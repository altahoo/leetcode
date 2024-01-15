# 299. Bulls and Cows

# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        s_counter = collections.Counter(list(secret))
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
                s_counter[s] -= 1
                if s_counter[s] < 0:
                    b -= 1
            elif s_counter[g] > 0:
                b += 1
                s_counter[g] -= 1
        return str(a) + 'A' + str(b) + 'B'