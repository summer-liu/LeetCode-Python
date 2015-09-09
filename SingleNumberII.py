class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1,2,2,2,3,3]
        """
        ones = twos = 0
        for n in nums:
        	ones = (ones ^ n) & ~twos
        	twos = (twos ^ n) & ~ones
        return ones
        