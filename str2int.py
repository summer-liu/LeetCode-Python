import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.strip()
        if not str:
        	return 0
        re_int = re.compile(r'^([+|-]?)(\d+)')
        match = re_int.match(str)
        if match:
        	groups = match.groups()
        	digits = sum([(ord(n) -  ord('0')) * 10**i for i,n in enumerate(reversed(groups[1]))])
	        sign = -1 if groups[0]=='-' else 1
	        value = sign*digits
	        if value > INT_MAX:
	        	return INT_MAX
	        elif value < INT_MIN:
	        	return INT_MIN
	        return value
        return 0
      

s = Solution()
str1 = '+123   '        
str2 = '  -3423aadfad3 d '
str3 = '  +odoaod'

print(s.myAtoi(str1))