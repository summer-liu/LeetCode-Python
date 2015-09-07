# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        fast = head
        slow = head
        if head is None or head.next is None:
        	return True
        while fast and fast.next and fast.next.next:
        	fast = fast.next.next
        	slow = slow.next
        second = slow.next
        slow.next = None
        p1 = second
        p2 = p1.next
        while p2:
        	tmp = p2.next
        	p2.next = p1
        	p1 = p2
        	p2 = tmp
        second.next = None
        p = p1
        q = head
        while p:
        	if p.val != q.val:
        		return False
        	p = p.next
        	q = q.next
        return True

