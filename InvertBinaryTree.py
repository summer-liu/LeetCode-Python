# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
        	return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


    def invertTree2(self, root):
    	stack = [root]
    	while stack:
    		node = stack.pop()
    		if node:
    			node.left, node.right = node.right, node.left
    			stack.append(node.left)
    			stack.append(node.right)
    	return root
