class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
    	invalid = 0
    	space = 1
    	sign = 2
    	digit = 3
    	dot = 4
    	exponent = 5
    	TransitionTable = [
    						[-1,0,3,1,2,-1],
    						[-1,8,-1,1,4,5],
    						[-1,-1,-1,4,-1,-1],
    						[-1,-1,-1,1,2,-1],
    						[-1,8,-1,4,-1,5],
    						[-1,-1,6,7,-1,-1],
    						[-1,-1,-1,7,-1,-1],
    						[-1,8,-1,7,-1,-1],
    						[-1,8,-1,-1,-1,-1]
    						]
    	state = 0
    	i = 0
    	while i < len(s):
    		inputtype = invalid
    		if s[i] == ' ':
    			inputtype = space
    		elif s[i] == "+" or s[i] == "-":
    			inputtype = sign
    		elif s[i] in "0123456789":
    			inputtype = digit
    		elif s[i] == ".":
    			inputtype = dot
    		elif s[i] == "e" or s[i] == "E":
    			inputtype = exponent

    		state = TransitionTable[state][inputtype]
    		if state == -1:
    			return False
    		else:
    			i += 1
    	return state == 1 or state == 4 or state == 7 or state == 8


 

S = Solution()
s = "1.1e1    "
a = S.isNumber(s)
print a


"""
import re
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
    	pattern = re.compile(r"^\s*\d*.?\d+(e|E\d+)?\s*$")
    	match = pattern.match(s)
    	if match:
    		return True
    	return False
"""        