class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        j = 0
        for i in range(n):
        	if nums[i] != val:
        		nums[j] = nums[i]
        		j += 1
        return j

s = Solution()
nums = [1, 2, 3, 4, 5, 3, 6,1]
print(s.removeElement(nums, 3))        
        