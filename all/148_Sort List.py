# 148. Sort List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Insertion sort, TLE
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        
        while head:
            tmp = head.next
            cur = dummy
            while cur.next and cur.next.val <= head.val:
                cur = cur.next

            cur.next = head
            head.next = cur.next
            head = tmp
        
        return dummy.next


# Merge sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(a,b):
            cur = res = ListNode()
            while a and b:
                if a.val <= b.val:
                    cur.next = a 
                    a = a.next 
                else:
                    cur.next = b 
                    b = b.next  
                cur = cur.next 
            cur.next = a or b   
            return res.next
        
        if not head or not head.next:
            return head 
        
        slow, fast = head, head 
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            
        second = slow.next
        slow.next = None
            
        first_half = self.sortList(head)
        second_half = self.sortList(second)
        result = merge(first_half, second_half)
        
        return result