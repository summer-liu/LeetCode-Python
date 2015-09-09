class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
        	return 0
        n = len(matrix[0])
        if n == 0:
        	return 0
        h = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == '1':
        			h[i][j] =  1 if i == 0 else h[i-1][j]+1
        		else:
        			h[i][j] = 0
        maxArea = 0
        for i in range(m):
        	maxArea = max(maxArea, self.largestRectangleArea(h[i]))
        return maxArea

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
