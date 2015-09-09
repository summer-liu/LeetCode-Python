# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    	res = []
    	self.dfs(root, res)
    	return res  
	def dfs(self, root, res):
		if root:
			self.dfs(root.left, res)
			res.append(root.val)
			self.dfs(root.right, res)


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		root = stack.pop()
        		res.append(root.val)
        		root = root.right
        return res