# 677. Map Sum Pairs

# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


class TrieNode:
    def __init__(self, val=0):
        self.children = [None] * 26
        self.value = val
        self.is_end = False
    

class MapSum:

    def __init__(self):
        self.trie = TrieNode()
        self.key_value = {}
    
    def __exists(self, key):
        cur = self.trie
        for i, letter in enumerate(key):
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                return 0
            value = cur.children[idx].value
            if i == len(key) - 1:
                return self.key_value[key] if cur.children[idx].is_end else 0
            cur = cur.children[idx]

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        existing_val = self.__exists(key)
        print(f'existing: {existing_val}')
        for i, letter in enumerate(key):
            idx = ord(letter) - ord('a')
            if cur.children[idx]:
                cur.children[idx].value += val - existing_val
            else:
                cur.children[idx] = TrieNode(val)
            if i == len(key) - 1:
                cur.children[idx].is_end = True
            cur = cur.children[idx]
        self.key_value[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for letter in prefix:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                return 0
            value = cur.children[idx].value
            cur = cur.children[idx]
            
        return value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)