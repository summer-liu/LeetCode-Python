# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxsum(self, root):
        if root == None: return 0
        lmax = self.maxsum(root.left)
        rmax = self.maxsum(root.right)
        Solution.max = max(Solution.max,root.val + lmax + rmax)
        return max(0, root.val, root.val + lmax, root.val + rmax)
    
    def maxPathSum(self, root):
        Solution.max = -10**10
        if root == None: return 0
        self.maxsum(root)
        return Solution.max