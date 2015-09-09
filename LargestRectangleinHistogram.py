class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        h = height[:]
        h.append(0)
        stack = []
        i = 0
        while i <len(h):
        	if not stack or h[i] >= h[stack[-1]]:
        		stack.append(i)
        		i += 1
        	else:
        		n = stack.pop()
        		maxArea = max(maxArea, h[n] * (i-stack[-1]-1 if stack else i))
        return maxArea
