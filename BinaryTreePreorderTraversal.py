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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

        # recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res

def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

        
          
        