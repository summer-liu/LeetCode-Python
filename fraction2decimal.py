class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if (type(numerator) != int) or (type(denominator) != int ):
        	raise TypeError('intput type must be int!')
        if denominator == 0:
        	raise ValueError('denominator can not  be 0!')
        if numerator % denominator == 0:
        	return str(numerator/denominator)
        
        nums = []
        negativeSign = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        table = dict()
        current = 0
        loop = None
        while True:
        	nums.append(str(numerator // denominator))
        	numerator = 10* (numerator % denominator)
        	current += 1
        	if numerator == 0:
        		break
        	loc = table.get(numerator)
        	if loc:
        		loop = ''.join(nums[loc:current])
        		break
        	table[numerator] = current
        ans = nums[0]
        if len(nums) > 1:
        	ans += "."
        if loop:
        	ans += ''.join(nums[1:len(nums)-len(loop)]) + '(' + loop + ')'
        else:
        	ans += ''.join(nums[1:])
        if negativeSign:
        	ans = '-' + ans
        return ans



s = Solution()
ans = s.fractionToDecimal(2,7)
print(ans)
