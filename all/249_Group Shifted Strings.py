# 249. Group Shifted Strings

# We can shift a string by shifting each of its letters to its successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        def shift_letter(letter, shift):
            return chr((ord(letter) - shift) % 26)

        def get_hash(str):
            shift = ord(str[0])
            return ''.join(shift_letter(letter, shift) for letter in str)
        
        for string in strings:
            key = get_hash(string)
            groups[key].append(string)
        
        return list(groups.values())