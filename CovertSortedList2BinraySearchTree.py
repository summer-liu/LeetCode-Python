# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        p = head
        while p is not None:
        	p = p.next
        	length += 1
        return self.helper(head, length, ListNode(0))
    def helper(self, head, length, node):
    	if length < 1:
    		node.next = head
    		return None
    	left = self.helper(head, length/2, node)
    	root = TreeNode(node.next.val)
    	node.next  = node.next.next
    	root.left = left
    	root.right = self.helper(node.next, length - length/2 - 1, node)
    	return root

        

