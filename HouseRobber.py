[3,4,6,7,1,3,2,4]
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        money = [0]*(n+1)
        if n:
        	money[1] = nums[0]
        for i in range(2,n+1):
            money[i] = max(money[i-1], money[i-2] + nums[i-1])
        return money[n]

        