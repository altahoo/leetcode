# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        result = 0
        while queue:
            cur = queue.popleft()
            result += 1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result