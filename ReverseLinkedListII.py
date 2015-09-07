# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        i = 1
        while i < m:
        	p = p.next
        	i += 1
        j = 0
        curr = p.next
        start = curr
        pre = None
        tmp = None
        while curr and (j < n-m+1):
        	tmp = curr.next
        	curr.next = pre
        	pre = curr
        	curr = tmp
        	j += 1
        p.next = pre
        start.next = tmp
        return dummy.next