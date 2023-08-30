# 433. Minimum Genetic Mutation

# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        step = 0
        queue = collections.deque([startGene])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endGene:
                    return step
                for i in range(len(cur)):
                    for ch in ['A', 'C', 'G', 'T']:
                        if ch == cur[i]:
                            continue
                        new_cur = cur[:i] + ch + cur[i + 1:]
                        if new_cur in bank and new_cur not in visited:
                            visited.add(new_cur)
                            queue.append(new_cur)
            step += 1
        return -1