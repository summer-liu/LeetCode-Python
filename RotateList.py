# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (type(k) != int) or k < 0:
        	raise ValueError('k must be non-negative integer')
        if head == None:
        	return None
        dummy = ListNode(0)
        dummy.next = head
        p = head
        length = 1
        while p.next:
        	p = p.next
        	length += 1
        k %= length
        if k == 0:
        	return head
        loc = 1
        q = head
        while loc < length - k:
        	q = q.next
        	loc += 1
        p.next = dummy.next
        dummy.next = q.next
        q.next = None
        return dummy.next





