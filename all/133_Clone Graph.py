# 133. Clone Graph

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = collections.deque([node])
        old_new_mapping = {}

        new_node = Node(node.val)
        old_new_mapping[node] = new_node

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old_new_mapping:
                    new_neighbor = Node(neighbor.val)
                    old_new_mapping[neighbor] = new_neighbor
                    old_new_mapping[cur].neighbors.append(new_neighbor)
                    queue.append(neighbor)
                else:
                    old_new_mapping[cur].neighbors.append(old_new_mapping[neighbor])
        
        return new_node