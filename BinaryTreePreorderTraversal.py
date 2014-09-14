# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        list = []
        stack = []
        if root:
            stack.append(root)
            while stack:
                node = stack.pop()
                list.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return list
                
            
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        list = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                list.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list

          
        