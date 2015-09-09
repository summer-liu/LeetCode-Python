class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.result = []
        lists = []
        self.dfs(s, lists)
        return Solution.result
    def dfs(self, s, lists):
    	if len(s) == 0:
    		Solution.result.append(lists)
    	for i in range(1, len(s)+1):
    		if self.isPalindrome(s[:i]):
    			self.dfs(s[i:], lists + [s[:i]])
    def isPalindrome(self, s):
    	for i in range(len(s)):
    		if s[i] != s[len(s)-1-i]:
    			return False
    	return True

print(Solution().partition('aab'))