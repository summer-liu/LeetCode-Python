class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	res = [[] for i in range(numRows)]
    	if numRows == 0:
    		return []
    	for i in range(numRows):
    		res[i] = [1 for j in range(i+1)]
    	for i in range(2,numRows):
    		for j in range(1,i):
    			res[i][j] = res[i-1][j-1] + res[i-1][j]
    	return res

s = Solution()
a = s.generate(5)
print a

        
        