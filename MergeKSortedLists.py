# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
        	if node is not None:
        		heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
        	top = heapq.heappop(heap)
        	curr.next = ListNode(top[0])
        	curr = curr.next
        	if top[1].next:
        		heapq.heappush(heap, (top[1].next.val, top[1].next))
        return head.next
