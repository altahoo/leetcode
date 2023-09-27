# 508. Most Frequent Subtree Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_freq = collections.defaultdict(int)
        self.max_count = 0

    def postorder(self, node):
        if not node:
            return 0
        left = self.postorder(node.left)
        right = self.postorder(node.right)
        subtree_sum = left + right + node.val
        self.sum_freq[subtree_sum] += 1
        self.max_count = max(self.max_count, self.sum_freq[subtree_sum])
        return subtree_sum

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder(root)
        result = []
        for subtree_sum, cnt in self.sum_freq.items():
            if cnt == self.max_count:
                result.append(subtree_sum)
        return result