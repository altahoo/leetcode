# 288. Unique Word Abbreviation

# The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

# For example:

# dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
# internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
# it --> it because any word with only two characters is an abbreviation of itself.
# Implement the ValidWordAbbr class:

# ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
# boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
# There is no word in dictionary whose abbreviation is equal to word's abbreviation.
# For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dict = collections.defaultdict(set)
        for word in dictionary:
            abbrev = self.get_abbreviation(word)
            self.dict[abbrev].add(word)
        

    def isUnique(self, word: str) -> bool:
        abv = self.get_abbreviation(word)
        if abv not in self.dict or self.dict[abv] == set([word]):
            return True
        return False

    def get_abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)