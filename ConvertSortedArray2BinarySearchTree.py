# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     if len(nums) == 0:
    #     	return None
    #     return self.middleNode(nums, 0, len(nums)-1)
    # def middleNode(self, num, start, end):
    # 	if start > end:
    # 		return None
    # 	root = TreeNode(num[start + (end-start)/2])
    # 	root.left = self.middleNode(num, start, start+(end-start)/2-1)
    # 	root.right = self.middleNode(num, start+(end-start)/2+1, end)
    # 	return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
        	return None
        elif len(nums) == 1:
        	return TreeNode(nums[0])
        else:
        	mid = len(nums)/2
        	root = TreeNode(nums[mid])
        	root.left = self.sortedArrayToBST(nums[:mid])
        	root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

