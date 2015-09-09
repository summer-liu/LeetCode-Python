# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        pre = root
        curr = None
        while pre and pre.left:
        	curr = pre
        	while curr:
        		curr.left.next = curr.right
        		if curr.next:
        			curr.right.next = curr.next.left
        		curr = curr.next
        	pre = pre.left

