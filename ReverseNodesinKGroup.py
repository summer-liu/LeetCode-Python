# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None or head.next is None or k == 1:
        	return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 0 
        while head != None:
        	i += 1
        	if(i%k == 0):
        		pre = self.reverse(pre, head.next)
        		head = pre.next
        	else:
        		head = head.next
        return dummy.next
    def reverse(self, pre, next):
    	last = pre.next
    	curr = last.next
    	while curr != next:
    		last.next = curr.next
    		curr.next = pre.next
    		pre.next = curr
    		curr = last.next
    	return last







