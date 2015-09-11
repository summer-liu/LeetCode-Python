class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        2 1 0 2 0 1 1 1
        """
        n = len(nums)
        if n == 0:
        	return False
        if n == 1:
        	return True
        if n == 2:
        	return nums[0] > 0
        curr = n - 2
        next = n - 1
        while curr >= 0:
        	if nums[curr] < next - curr:
        		curr -= 1
        	else:
        		next = curr
        		curr -= 1
        		if curr < 0:
        			return True
        return False

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        2 1 3 2 0 1 1 1
        """
        n = len(nums)
        i = 0
        reach = 0
        while i < n and i <= reach:
        	reach = max(reach, i + nums[i])
        	i += 1
        return i == n

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last = n - 1
        for i in range(n-2, -1, -1):
        	if i + nums[i] >= last:
        		last = i
        return last == 0
