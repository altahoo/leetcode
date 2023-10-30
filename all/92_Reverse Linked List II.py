# 92. Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head
        i = left - 1
        while i:
            prev = prev.next
            i -= 1
        
        cur = prev.next
        i = right - left
        while i > 0:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            i -= 1
        return new_head.next
