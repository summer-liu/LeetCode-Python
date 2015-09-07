# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
        	return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        current = dummy.next
        while current:
        	if current.val == val:
        		p.next = current.next
        	else:
        		p = p.next
        	current = current.next
        return dummy.next


        