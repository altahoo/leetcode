# 129. Sum Root to Leaf Numbers


# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((root, str(root.val)))
        result = 0
        while queue:
            for _ in range(len(queue)):
                node, val = queue.popleft()
                if not node.right and not node.left:
                    result += int(val)
                if node.left:
                    queue.append((node.left, val + str(node.left.val)))
                if node.right:
                    queue.append((node.right, val + str(node.right.val)))
        return result