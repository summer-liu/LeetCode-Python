class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
		if n == 0:
			return 1
		if n == 1:
			return x
		if n < 0:
		    return 1/self.pow(x,-n)
		return self.pow(x,n/2)**2*self.pow(x,n%2)        

s = Solution()
a = s.pow(3,5)
print a