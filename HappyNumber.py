class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        while n != 1:
        	if n in stack:
        		return False
        	else:
        		stack.append(n)
        	tmp = 0
        	while n:
        		tmp += (n%10)**2
        		n = n//10
        	n = tmp
        return True
s = Solution()
print(s.isHappy(134))




