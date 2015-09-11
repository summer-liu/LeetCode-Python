class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        1  2  3  4  5
        6  7  8  9  10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25
        """
        m = len(matrix)
        if m == 0:
        	return []
        n = len(matrix[0])
        if n == 0:
        	return []
        res = []
        up = left = 0
        down = m - 1
        right = n - 1
        direct = 0
        while True:
        	if direct == 0:
        		for i in range(left, right + 1):
        			res.append(matrix[up][i])
        		up += 1
        	if direct == 1:
        		for i in range(up, down + 1):
        			res.append(matrix[i][right])
        		right -= 1
        	if direct == 2:
        		for i in range(right, left - 1, -1):
        			res.append(matrix[down][i])
        		down -= 1
        	if direct == 3:
        		for i in range(down, up - 1, -1):
        			res.append(matrix[i][left])
        		left += 1
        	if up > down or left > right:
        		return res
        	direct = (direct + 1) % 4