class Solution:
    # @param n, an integer
    # @return an integer
    # Dynamic programming
    def climbStairs(self, n):
    	dp=[1 for i in range(n+1)]
    	for i in range(2,n+1):
    		dp[i] = dp[i-1] + dp[i-2]
    	return dp[n]




class Solution2:
    # @param n, an integer
    # @return an integer
    # Combination
    def climbStairs(self, n):
    	if n == 1:
    		return 1
    	count2 = 0
    	num2 = n/2
    	res = 1
    	for i in range(1,num2+1):
    		s = n - i*2 + i
    		if n == i*2:
    			res += 1
    		else:
    			res +=  self.factorial(s)/(self.factorial(i)*self.factorial(s-i))
    	return res

    def factorial(self,n):
    	if n == 0:
    		return 0
    	if n == 1:
    		return 1
    	return n*self.factorial(n-1)



s = Solution()
a = s.climbStairs(2)
print a