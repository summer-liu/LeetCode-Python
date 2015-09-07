# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # pre = None
        # curr = head
        # while curr != None:
        # 	temp = curr.next
        # 	curr.next = pre
        # 	pre = curr
        # 	curr = temp
        # head = prev
        # retun head
        if head is None  or head.next is None:
        	return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
