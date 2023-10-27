# 82. Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

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
            duplicate = False
            while head.next and head.val == head.next.val:
                head = head.next
                duplicate = True
            if duplicate:
                head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = None
        return dummy.next
