# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the head of the second half
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        cur = second
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        second = prev
        first = head

        # Connect first and second
        i = 0
        dummy = ListNode(0)
        cur = dummy
        while first and second:
            if i % 2 == 0:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next
            i += 1
        
        if first:
            cur.next = first
        
        if second:
            cur.next = second
        
        return dummy.next