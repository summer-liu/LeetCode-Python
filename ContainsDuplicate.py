class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = dict()
        for n in nums:
        	if n in table:
        		return True
        	else:
        		table[n] = 1
        return False
        # return len(nums) > len(set(nums))
