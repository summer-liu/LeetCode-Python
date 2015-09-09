class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0]*(n+1)
        nums[0] = nums[1] = 1
        for i in range(2,n+1):
        	for j in range(i):
        		nums[i] += nums[j]*nums[i-j-1]
        return nums[n]
        	