# 68. Text Justification

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_line = []
        cur_len = 0
        result = []
        for word in words:
            cur_len += len(word)
            num_cur_words = len(cur_line)
            if cur_len + num_cur_words < maxWidth:
                cur_line.append(word)
                continue
            if cur_len + num_cur_words == maxWidth:
                cur_line.append(word)
                result.append(' '.join(cur_line))
                cur_line = []
                cur_len = 0
                continue
            cur_len -= len(word)
            num_space = (maxWidth - cur_len) // (num_cur_words - 1) if num_cur_words > 1 else (maxWidth - cur_len)
            extra = (maxWidth - cur_len) % (num_cur_words - 1) if num_cur_words > 1 else 0
            line = ''
            for i in range(num_cur_words):
                line += cur_line[i]
                if i < extra:
                    line += (1 + num_space) * ' '
                elif i < num_cur_words - 1 or num_cur_words == 1:
                    line += ' ' * num_space
            result.append(line)       
            cur_line = [word]
            cur_len = len(word)
        
        if cur_line:
            result.append(' '.join(cur_line) + ' ' * (maxWidth - cur_len - len(cur_line) + 1))
        return result
