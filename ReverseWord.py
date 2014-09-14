class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
    	return ' '.join(s.split()[::-1])


s = Solution()
a = s.reverseWords("the sky is blue")
print a