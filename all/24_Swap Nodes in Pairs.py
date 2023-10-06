# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        dummy = prev
        prev.next = head
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            # swith first and second
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next
