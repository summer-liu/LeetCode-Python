# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	return self.getSum(root,0)

    def getSum(self, root, preSum):
    	if root == None:
    		return 0
    	preSum = preSum*10 + root.val    		
    	if root.left == None and root.right == None:
    		return preSum
    	return self.getSum(root.left,preSum) + self.getSum(root.right,preSum)


"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	sum, depth = self.helper(root)
    	res = sum + sum([root.val * 10**i for i in depth])
    	return res


    def helper(self,root):
    	if root == None:
    		return 0,[0]
    	if root.left == None and root.right == None:
    		return root.val, [1]
    	if root.left == None and root.right != None:
    		sum,depth = self.helper(root.right)
    		sum = sum + sum([root.val*10**i for i in depth])
    		depth = [i+1 for i in depth]
    		return sum,depth
		if root.right == None and root.left != None:
			sum,depth = self.helper(root.left)
			sum = sum + sum([root.val*10**i for i in depth])
			depth = [i+1 for i in depth]
			return sum,depth

    	sumLeft, depthLeft = self.helper(root.left)
    	sumRight, depthRight = self.helper(root.right)

    	sum = sumLeft + sumRight + sum([root.val*10**i for i in depthLeft]) + sum([root.val*10**i for i in depthRight])
    	depth = [i+1 for i in depthLeft] + [i+1 for i in depthRight]

    	return sum,depth
"""   