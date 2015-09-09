class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ending = soFar = nums[0]
        for x in nums[1:]:
            ending = max(x, ending + x )
            soFar = max(soFar, ending)
        return soFar
        
        