class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
    	return self.helper(range(1,n+1),k)



    def helper(self, A, k):
    	n = len(A)
    	if A == None:
    		return None
        if k == 0:
            return [[] for i in A]
        if k > n:
            return None
        if k == n:
            return [A]
        if k == 1:
        	#print [[i] for i in A]
        	return [[i] for i in A]
        res = []
    	for i in range(n-1):
    		if k>1:
    			print A[i+1:]
    			print k
    			tmp = self.helper(A[i+1:],k-1)
    			#print tmp
    			new= [[A[i]]+j for j in tmp]
    		res += new	#print res
        return res    	



        
s = Solution()
a = s.combine(4,3) 
print a       