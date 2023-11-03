# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        def constructTree(in_start, in_end, pre_start):
            if in_start > in_end:
                return None
            
            root = TreeNode(preorder[pre_start])
            root_idx = 0
            for i in range(in_start, in_end + 1):
                if inorder[i] == root.val:
                    root_idx = i
                    break
            root.left = constructTree(in_start, root_idx - 1, pre_start + 1)
            root.right = constructTree(root_idx + 1, in_end, pre_start + 1 + root_idx - in_start)

            return root
        return constructTree(0, len(inorder) - 1, 0)
