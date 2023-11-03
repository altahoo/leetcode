# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def buildBST(start, end):
            if start > end:
                return None
            
            mid = start + (end - start) // 2
            root = TreeNode(
                val=nums[mid],
                left=buildBST(start, mid - 1),
                right=buildBST(mid + 1, end)
            )
            return root
        return buildBST(0, n - 1)
