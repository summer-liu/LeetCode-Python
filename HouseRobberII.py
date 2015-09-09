class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
        	return 0
        if n < 4:
        	return max(nums)
        last = now = 0
        for i in nums[:-1]:
        	last, now = now, max(last + i, now)
        max1 = now
        last = now = 0
        for i in nums[1:]:
        	last, now = now, max(last + i, now)
        return max(max1, now)
