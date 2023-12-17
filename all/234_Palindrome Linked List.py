# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half

        prev = None
        cur = slow.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # prev is the new head of the second half
        first, second = head, prev
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True