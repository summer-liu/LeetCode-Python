class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
        	if (nums[i] != (i + 1)) and  (1 <= nums[i] <= n) and (nums[nums[i]-1] != nums[i]):
        		tmp = nums[i]
        		nums[i] =  nums[tmp-1]
        		nums[tmp-1]  = tmp
        	else:
        		i += 1
        for i in range(n):
        	if nums[i] != (i + 1):
        		return i + 1
        return n + 1

nums = [3,4,-1,1]
print(Solution().firstMissingPositive(nums))