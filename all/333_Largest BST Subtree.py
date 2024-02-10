# 333. Largest BST Subtree

# Given the root of a binary tree, find the largest 
# subtree
# , which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

# The left subtree values are less than the value of their parent (root) node's value.
# The right subtree values are greater than the value of their parent (root) node's value.
# Note: A subtree must include all of its descendants.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ETL
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def is_bst(node):
            if not node:
                return True
            
            def find_max(node):
                if not node:
                    return float('-inf')
                return max(node.val, find_max(node.left), find_max(node.right))
            
            def find_min(node):
                if not node:
                    return float('inf')
                return min(node.val, find_min(node.left), find_min(node.right))
            
            left_max = find_max(node.left) # max node value in node's left subtree
            if left_max >= node.val:
                return False

            right_min = find_min(node.right) # min node value in node's right subtree
            if right_min <= node.val:
                return False
            
            return is_bst(node.left) and is_bst(node.right)
        
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
            
        if not root:
            return 0
        
        if is_bst(root):
            return count_nodes(root)
        
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))



# Improve is_bst() from O(n^2) to O(n)
class Solution:
    def is_bst(self, node):
        if not node:
            return True
        
        if not self.is_bst(node.left):
            return False
        
        if self.prev and self.prev.val >= node.val:
            return False
        
        self.prev = node
        return self.is_bst(node.right)
        
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
            
        if not root:
            return 0
        
        self.prev = None
        
        if self.is_bst(root):
            return count_nodes(root)


# Improve # 2, 不太懂