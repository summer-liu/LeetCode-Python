class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,2,2,3,4,3]
        """
        for i in range(1, len(nums)):
        	nums[0] ^= nums[i]
        return nums[0]
