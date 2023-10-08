# 25. Reverse Nodes in k-Group

# [1, 2, 3, 4, 5]  k = 3

# -1->1->2->3->4->5
#  |        |  |
# start    end next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy
        
        while True:
            end = self.getEndNode(start, k)
            if not end:
                return dummy.next
            next = end.next

            # start: one node before the current group, 
            # end: the last node of the current group
            # next: one node after the current group
            # Reverse the current k group
            prev, curr = end.next, start.next
            while curr != next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            start.next, start = end, start.next
        return dummy.next
    
    def getEndNode(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node