# # 211. Design Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_word = True
    

    def searchWord(self, word, node):
        for i, letter in enumerate(word):
            if letter not in node.children:
                if letter == '.':
                    for c in node.children:
                        if self.searchWord(word[i + 1:], node.children[c]):
                            return True
                return False
            else:
                node = node.children[letter]
        return node.is_word

    def search(self, word: str) -> bool:

        def dfs(node, idx):
            if idx == len(word):
                return node.is_word
            
            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
            
            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx + 1)
            
            return False
        
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)