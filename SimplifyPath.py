class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
    	stack = ['/']
    	for i in path.strip('/').split('/'):
    		if i == '' or i == '.':
    			continue
    		if i == '..':
    			if len(stack)>1:
    				stack.pop()
    		else:
    			stack.append(i + '/')
    	return ''.join(stack).rstrip('/') if len(stack) > 1 else ''.join(stack)



s  = Solution()
path = '/summer/tao /..///./c'
a = s.simplifyPath(path)
print a     