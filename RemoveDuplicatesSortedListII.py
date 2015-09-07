# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return None
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp.next is not None and tmp.next.next is not None:
        	if tmp.next.val == tmp.next.next.val:
        		val = tmp.next.val
        		while tmp.next and tmp.next.val == val:
        			tmp.next = tmp.next.next
        	else:
        		tmp = tmp.next
        return dummy.next

        