# 269. Alien Dictionary

# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
# sorted lexicographically
#  by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.graph = collections.defaultdict(set)
        self.indegree = collections.defaultdict(int)

        def buildGraph():
            for word in words:
                for letter in word:
                    self.indegree[letter] = 0

            for i in range(1, len(words)):
                prev = words[i - 1]
                cur = words[i]

                found_diff = False
                for j in range(min(len(prev), len(cur))):
                    if prev[j] == cur[j]:
                        continue
                    fournd_diff = True

                    if cur[j] not in self.graph[prev[j]]:
                        self.graph[prev[j]].add(cur[j])
                        self.indegree[cur[j]] += 1
                    break
                
                if not found_diff and len(prev) > len(cur) and prev[:len(cur)] == cur:
                    self.indegree = []
                    break
        
        buildGraph()
        if not self.indegree:
            return ''

        result = []
        # BFS
        queue = collections.deque([])
        for letter, in_degree in self.indegree.items():
            if in_degree == 0:
                queue.append(letter)
        
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for next_letter in self.graph[cur]:
                self.indegree[next_letter] -= 1
                if self.indegree[next_letter] == 0:
                    queue.append(next_letter)
        
        return ''.join(result) if len(result) == len(self.indegree) else ''
