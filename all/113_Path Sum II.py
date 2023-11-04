# 113. Path Sum II

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        sol = []

        def _find_path(node, sol):
            if not node:
                return
            
            if not node.left and not node.right:
                if sum(sol) + node.val == targetSum:
                    sol.append(node.val)
                    result.append(sol)
                    return
            
            if node.left:
                _find_path(node.left, sol + [node.val])
            
            if node.right:
                _find_path(node.right, sol + [node.val])
            
        _find_path(root, [])
        
        return result