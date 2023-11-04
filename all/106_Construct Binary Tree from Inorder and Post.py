# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return []

        def _buildBST(in_start, in_end, post_end):
            if in_start > in_end:
                return None
            
            root_val = postorder[post_end]
            in_idx = 0
            for i in range(in_start, in_end + 1):
                if inorder[i] == root_val:
                    in_idx = i
                    break
            root = TreeNode(root_val)
            root.left = _buildBST(in_start, in_idx - 1, post_end - in_end + in_idx - 1)
            root.right = _buildBST(in_idx + 1, in_end, post_end - 1)
            return root