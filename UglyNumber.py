class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (type(num) != int) or num < 1:
        	return False
      
        for n in [2,3,5]:
        	while num % n == 0:
        		num /= n
        return num == 1

