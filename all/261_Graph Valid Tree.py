# 261. Graph Valid Tree

# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Fully connected and no cycle
        # For the graph to be a valid tree, it must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a) 
        
        # The graph shold be fully connected
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n
