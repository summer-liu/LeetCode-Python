class Solution:
    # @return a boolean
    def isValid(self, s):
    	stack = []
    	for i in s:
    		if len(stack) and ((stack[-1] =='(' and i == ')') or (stack[-1] =='{' and i == '}') or (stack[-1] =='[' and i == ']')):
    			stack.pop()
    		else:
    			stack.append(i)
    	if len(stack):
    		return False
    	return True




s = Solution()
a = s.isValid('([])[]{}')
print a
        