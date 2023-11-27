# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA, lB = 0, 0
        cur = headA
        while cur:
            lA += 1
            cur = cur.next
        
        cur = headB
        while cur:
            lB += 1
            cur = cur.next
        
        if lA > lB:
            headA, headB = headB, headA
            lA, lB = lB, lA
        
        diff = lB - lA
        curB = headB
        while diff:
            curB = curB.next
            diff -= 1
        
        curA = headA
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB

        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA
        