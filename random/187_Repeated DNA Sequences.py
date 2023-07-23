# 187. Repeated DNA Sequences

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_count = collections.defaultdict(int)
        result = set()
        for i in range(len(s) - 9):
            seq = s[i: i + 10]
            seq_count[seq] += 1
            if seq_count[seq] > 1:
                result.add(seq)
        return list(result)
