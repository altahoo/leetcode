# 109. Convert Sorted List to Binary Search Tree

# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        self.head = head

        def buildBST(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            left = buildBST(start, mid - 1)
            root = ListNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = buildBST(mid + 1, end)
            return root
        
        return buildBST(0, length - 1)