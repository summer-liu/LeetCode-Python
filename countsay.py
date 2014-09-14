class Solution:
	def cut(s):
		for i in range(len(s)):
			if (s[i] != s[0]):
				return i
		return len(s)

	def count(self,n):
		if (n == 1):
			return "1"
		res = ""
		s = count(n-1)

		while(s ):
			j = cut(s)
			res +="{0}{1}".format(j,s[0])
			s = s[j:]
			





s = Solution()
a = s.count(4)
print a 
