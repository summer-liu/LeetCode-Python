class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
        	for j in range(1,n):
        		dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
s = Solution()
a = s.uniquePaths(4,3)
print(a)