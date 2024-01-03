# 270. Closest Binary Search Tree Value

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        result = root.val
        while root:
            result = min(root.val, result, key = lambda x: (abs(x - target), x))
            root = root.left if target < root.val else root.right

        return result