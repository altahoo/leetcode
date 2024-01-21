# 314. Binary Tree Vertical Order Traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        table = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()
            table[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        return [table[x] for x in range(min_col, max_col + 1)]