class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        count[32] = {0}
        result = 0
        for i in range(0,32):
        	for j in range(0,len(A)):
        		if ((A[j]>>i)&1):
        			count[i] += 1
        	result  |= ((count[i]%3) << i)
       return result

s = Solution()
a = s.singleNumber([2,4,5,2,2,5,5])
print a