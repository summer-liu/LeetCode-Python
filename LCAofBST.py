# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
        	return None
        while (root.val - p.val) * (root.val - q.val) > 0:
        	root = (root.left, root.right)[p.val > root.val]
        return root
        # if p.val < root.val > q.val:
        # 	return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val < q.val:
        # 	return self.lowestCommonAncestor(root.right, p, q)
        # return root

