# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        k %= length
        if k == 0:
            return head
        
        slow, fast = head, head
        gap = k
        while gap:
            fast = fast.next
            gap -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        second = slow.next
        slow.next = None

        new_head = second
        while second.next:
            second = second.next
        
        second.next = head
        return new_head
        