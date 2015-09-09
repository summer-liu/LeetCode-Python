class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxLen = 0
        for i in range(len(s)):
        	if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
        		stack.pop()
        		maxLen = max(maxLen, i - stack[-1])
        	else:
        		stack.append(i)
        return maxLen

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
        	return 0
        dp = [0] * n
        maxLen = 0
        for i in range(n-2, -1, -1):
        	if s[i] == '(':
        		j = i + 1 + dp[i+1]
        		if (j < n and s[j] == ')'):
        			dp[i] = dp[i+1] + 2
	        		if j + 1 < n:
	        			dp[i] += dp[j+1]
        	maxLen = max(maxLen, dp[i])
        return maxLen



print(Solution().longestValidParentheses('(())((()'))        