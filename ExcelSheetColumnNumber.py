class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
    	l = len(s)
    	r = 0
    	for i in range(l):
    		r += int(ord(s[i])-64) * (26**(l-i-1))
    	return r
s = Solution()
a = s.titleToNumber('AB')
print a


        
        