class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
    	n = len(A)
    	if n == 0:
    		return None
    	if n == 1:
    		return A[0]
    	dpP = [0]*n
    	dpN = [0]*n
    	dpP[0] = A[0] if A[0] > 0 else 0
    	dpN[0] = 0 if A[0] > 0 else A[0]
    	for i in range(1,n):
    		if A[i] >= 0:
    			dpP[i] = max(dpP[i-1]*A[i], A[i])
    			dpN[i] = dpN[i-1] * A[i]
    		if A[i] < 0:
    			dpP[i] = dpN[i-1] * A[i]
    			dpN[i] = min(dpP[i-1] * A[i], A[i])
    	return max(dpP)



s = Solution()
A = [2,3,0.5,-2,8,-5,-9]
a = s.maxProduct(A)
print a       
        