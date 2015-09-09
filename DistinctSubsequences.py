class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        # dp = [[0 for i in range(ls+1)] for i in range(lt + 1)]
        # for i in range(ls+1):
        # 	dp[0][i] = 1
        # for i in range(1,lt+1):
        # 	for j in range(1,ls+1):
        # 		if(t[i-1] != s[j-1]):
        # 			dp[i][j] = dp[i][j-1]
        # 		else:
        # 			dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        # return dp[lt][ls]

        curRow = [0] * (ls + 1)
        preRow = [1] * (ls + 1)
        for i in range(1, lt + 1):
        	for j in range(1, ls + 1):
        		if(t[i-1] != s[j-1]):
        			curRow[j] = curRow[j-1]
        		else:
        			curRow[j] = curRow[j-1] + preRow[j-1]
        	preRow = curRow[:]
        return preRow[ls]

