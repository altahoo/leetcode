# 648. Replace Words

# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = collections.defaultdict(list)
        for root in dictionary:
            first = root[0]
            roots[first].append(root)
        
        for first, words in roots.items():
            words.sort(key=len)
        
        result = []
        for word in sentence.split():
            first = word[0]
            found = False
            for root in roots[first]:
                if word.startswith(root):
                    result.append(root)
                    found = True
                    break
            if not found:
                result.append(word)
        
        return ' '.join(result)