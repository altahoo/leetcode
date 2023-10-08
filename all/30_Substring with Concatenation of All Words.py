# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_cnt = collections.Counter(words)
        len_word = len(words[0])
        n_words = len(words)
        len_s = len(s)

        result = []
        for i in range(len_s - n_words * len_word + 1):
            str_cnt = collections.defaultdict(int)
            j = 0
            while j < n_words:
                str = s[i + j * len_word: i + (j + 1) * len_word]
                if not word_cnt[str]:
                    break
                str_cnt[str] += 1
                if str_cnt[str] > word_cnt[str]:
                    break
                j += 1
            if j == n_words:
                result.append(i)
        return result