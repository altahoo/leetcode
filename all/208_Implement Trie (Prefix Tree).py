# 208. Implement Trie (Prefix Tree)

class TrieNode:

    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        print(self.root, [i.val for i in self.root.children])

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(val=letter)
            cur = cur.children[letter]
        cur.is_word = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True