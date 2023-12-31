# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                cur = node.right