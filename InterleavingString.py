class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
        	return False
        dp = [[False for i in range(l2+1)] for i in range(l1+1)]
        for i in range(l1+1):
        	for j in range(l2+1):
        		if i == 0 and j == 0:
        			dp[i][j] = True
        		elif i == 0:
        			dp[i][j] = s2[:j] == s3[:j]
        		elif j == 0:
        			dp[i][j] = s1[:i] == s3[:i]
        		else:
        			dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
