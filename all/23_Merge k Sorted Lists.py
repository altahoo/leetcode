# 23. Merge k Sorted Lists

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heap.append((node.val, idx))
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            min_val, idx = heapq.heappop(heap)
            curr.next = ListNode(min_val)
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))
            curr = curr.next
        return dummy.next
