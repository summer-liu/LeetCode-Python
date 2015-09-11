# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
        	return []
        res = []
        self.dfs(root, str(root.val), res)
        return res
    def dfs(self, root, path, res):
    	if root.left is None and root.right is None:
    		res.append(path)
    	if root.left:
    		self.dfs(root.left, path + '->' + str(root.left.val), res)
    	if root.right:
    		self.dfs(root.right, path + '->' + str(root.right.val), res)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
        	return []
        res = []
        stack = [(root, str(root.val))]
        while stack:
        	node, path = stack.pop()
        	if node.left is None and node.right is None:
        		res.append(path)
        	if node.left:
        		stack.append((node.left, path + '->' + str(node.left.val)))
        	if node.right:
        		stack.append((node.right, path + '->' + str(node.right.val)))
        return res

