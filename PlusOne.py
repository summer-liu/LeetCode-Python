class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
    	n = len(digits)
    	res = []
    	if digits[n-1] != 9:
    		digits[n-1] += 1
    		return digits
    	digits[n-1] = 0
    	carry = 1
    	digits = digits[::-1]

    	for i in range(1,n):
    		digits[i] += carry
    		carry = digits[i]/10
    		digits[i] %= 10
    	if carry == 1:
    		digits.append(1)
    	return digits[::-1]





s = Solution()
a = s.plusOne([9,9,8])
print a
        