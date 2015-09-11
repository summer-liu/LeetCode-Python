class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        0 1 2 2 4 5 6 7
        2 4 5 6 7 0 1 2 
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
        	if nums[low] < nums[high]:
        		return nums[low]
        	mid = low + (high - low) // 2
        	if nums[mid] > nums[high]:
        		low = mid + 1
        	elif nums[mid] < nums[high]:
        		high = mid
        	else:
        		high -= 1
        return nums[low]