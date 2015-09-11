class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        4 5 6 7 0 1 2
        6 7 0 1 2 3 4
        5 6 7 8 1 2 3 4
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
        	if(nums[low] < nums[high]):
        		return nums[low]
        	mid = low + (high - low) // 2
        	if nums[mid] > nums[high]:
        		low = mid + 1
        	else:
        		high = mid
        return nums[low]

nums = [4,5,6,7,8,9, 0, 2,3]
print(Solution().findMin(nums))


