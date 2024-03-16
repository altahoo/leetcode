# 314. Binary Tree Vertical Order Traversal

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
        while queue:
            node, col = queue.popleft()
            table[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        return [i[1] for i in sorted(table.items())]


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        table = collections.defaultdict(list)
        min_col, max_col = float('inf'), -float('inf')

        queue = collections.deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            table[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [table[i] for i in range(min_col, max_col + 1)]
