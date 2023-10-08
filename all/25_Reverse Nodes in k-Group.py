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
            new_start = end.next

            curr, next = start.next, end.next
            while curr != new_start:
                tmp = curr.next
                curr.next = next
                next = curr
                curr = tmp
            
            tmp = start.next
            start.next = end
            start = tmp
        return dummy.next
    
    def getEndNode(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node