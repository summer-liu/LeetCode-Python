class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if not p:
        # 	return not s
        # if not s:
        # 	return len(p) == 2 and p[1] == '*'
        # if len(p) > 1 and p[1] == '*':
        # 	return (len(p) > 1 and self.isMatch(s, p[2:])) or (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p)
        # else:
        # 	return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:]) 
        # aab  a*b
        ls = len(s)
        lp = len(p)
        dp = [[False for i in range(lp+1)] for j in range(ls+1)]
        dp[0][0] = True
        for i in range(1, lp+1):
        	if p[i-1] == '*' and i > 1:
        		dp[0][i] = dp[0][i-2]
        for i in range(1, ls + 1):
        	for j in range(1, lp + 1):
        		if p[j-1] != '*':
        			dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        		else:
        			dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[-1][-1]


