# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
        	return None
        leftDummy = ListNode(0)
        left = leftDummy
        rightDummy = ListNode(0)
        right = rightDummy
        node = head
        while node:
        	if node.val < x:
        		left.next = node
        		left = left.next
        	else:
        		right.next = node
        		right = right.next
        	node = node.next
        right.next = None
        left.next = rightDummy.next
        return leftDummy.next
        # if head is None or head.next is None:
        # 	return head
        # dummy = ListNode(0)
        # dummy.next = head
        # p = dummy
        # low = p
        # while p.next:
        # 	if p.next.val < x:
        # 		if low.next == p.next:
        # 			p = p.next
        # 			low = low.next
        # 		else:	
	       #  		tmp1 = low.next
	       #  		tmp2 = p.next.next
	       #  		low.next = p.next
	       #  		low.next.next = tmp1
	       #  		p.next = tmp2
	       #  		low = low.next
        # 	else:
        # 		p = p.next
        # return dummy.next