class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
        	return 0
        last = curr = 0
        jump = i = 0
        while curr < n - 1:
        	while i <= last:
        		curr = max(curr, i + nums[i])
        		i += 1
        	if last == curr:
        		return -1
        	last = curr
        	jump += 1
        return jump