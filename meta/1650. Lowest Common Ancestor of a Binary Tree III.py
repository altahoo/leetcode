# 1650. Lowest Common Ancestor of a Binary Tree III

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself).



# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def depth(node):
            depth = 0
            while node.parent:
                depth += 1
                node = node.parent
            return depth
        
        p_depth = depth(p)
        q_depth = depth(q)
        
        if p_depth < q_depth:
            p, q = q, p
            p_depth, q_depth = q_depth, p_depth
        
        i = p_depth - q_depth
        while i:
            p = p.parent
            i -= 1
        
        if p == q:
            return q
        
        while p.parent != q.parent:
            p = p.parent
            q = q.parent
        return p.parent
