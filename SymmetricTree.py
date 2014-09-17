# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.helper(root.left,root.right)
        
    def helper(self,left,right):
        if left == None and right == None:
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return self.helper(left.left,right.right) and self.helper(right.left,left.right)
        
        