# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	h1 = headA
    	h2 = headB
    	res = null
    	if h1.val == h2.val:
    		res = h1.val
    	else:
    		while h1.next and h2.next:
	    		if h1.next.val == h2.next.val:
	    			res= h1.next.val
	    		else:
	    			h1 = h1.next
	    			h2 = h2.next
    	return res



