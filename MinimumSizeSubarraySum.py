class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = right = sums = 0
        l = n + 1
        while right < n:
        	while right < n and sums < s:
        		sums += nums[right]
        		right += 1
        	while left < end and sums >= s:
        		l = min(l, right - left)
        		sums -= nums[left]
        		left += 1
        return [0, l][l < n + 1]


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n
        l = 0
        while left <= right:
        	mid = (left + right) // 2
        	if self.search(nums, s, mid):
        		l = mid
        		right = mid - 1
        	else:
        		left = mid + 1
        return l

    def search(self, nums, s, mid):
    	sums = 0
    	for i in range(len(sums)):
    		sums += nums[i]
    		if x >= mid:
    			sums -= nums[i-mid]
    		if sums >= s:
    			return True
    	return False

