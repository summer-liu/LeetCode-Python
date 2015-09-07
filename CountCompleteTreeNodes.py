# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
        	return 0
        hl = 0
        hr = 0
        left = root
        right = root
        while left:
        	hl += 1
        	left = left.left
        while right:
        	hr += 1
        	right = right.right
        if hl == hr:
        	return 2**hl -1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1