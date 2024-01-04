# 272. Closest Binary Search Tree Value II

# Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        min_heap = []

        def dfs(node):
            if not node:
                return
            min_heap.append((abs(node.val - target), node.val))
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        heapq.heapify(min_heap)
        result = []
        while len(result) < k:
            result.append(heapq.heappop(min_heap)[1])
        return result