class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        if n == 0:
        	return []
        pre = 0
        cur = 0
        i = 1
        while i < n:
        	if nums[i] - nums[i-1] == 1:
        		cur = i
        		i += 1 
        	else:
        		if cur > pre:
        			res.append(str(nums[pre]) + "->" + str(nums[cur]))
        		else:
        			res.append(str(nums[pre]))
        		pre = i
        		cur = i
        		i += 1
        if cur > pre:
        	res.append(str(nums[pre]) + "->" + str(nums[cur]))
        else:
        	res.append(str(nums[pre]))        
        return res

def summaryRanges(nums):
	ranges = []
	for n in nums:
		if not ranges or n > ranges[-1][-1] + 1:
			ranges += [],
		ranges[-1][1:] = n,
	return ['->'.join(map(str, i)) for i in ranges]

nums = [0,1,2,4,5,7,9,10,12]
print(summaryRanges(nums))        		
        			      		

        	 
