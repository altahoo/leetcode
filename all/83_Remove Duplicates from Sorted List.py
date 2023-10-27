# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1000)
        cur = dummy
        while head:
            if head.val != cur.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None  
        return dummy.next