class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
        	return 0
        dp = [1] * (n+1)
        for i in range(2, n + 1):
        	if 10<int(s[i-2:i])<= 26 and s[i-1] != '0':
        		dp[i] = dp[i-1] + dp[i-2]
        	elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
        		dp[i] = dp[i-2]
        	elif s[i-1] != '0':
        		dp[i] = dp[i-1]
        	else:
        		dp[i] = 0
        return dp[-1]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
        	return 0
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 0 if s[n-1] == '0' else 1
        for i in range(n-2, -1, -1):
        	if s[i] == '0':
        		continue
        	else:
        		dp[i] = dp[i+1] + dp[i+2]  if (int(s[i:i+2]) <= 26) else dp[i+1]
        return dp[0]
