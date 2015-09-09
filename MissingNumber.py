class Solution(object):
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     [0,4,7,2,1,6,5] -> 3
    #     """
    #     n = len(nums)
    #     sums = n*(n+1)//2
    #     # for i in nums:
    #     # 	sums =  sums - i
    #     # return sums
    #     return sums - sum(nums)
    def missingNumber(self, nums):
    	res = len(nums)
    	for n,i in enumerate(nums):
    		res ^= n
    		res ^= i
    	return res


s = Solution()
# nums = [0,4,7,2,1,6,5] 
nums = [1,0,2,4,6,5]    
print(s.missingNumber(nums))
