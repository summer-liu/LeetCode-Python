class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix= [[0 for i in range(n)] for j in range(n)]
        up = left = 0
        down = right = n - 1
        direct = 0
        j = 1
        while True:
        	if direct == 0:
        		for i in range(left, right + 1):
        			matrix[up][i] = j
        			j += 1
        		up += 1
        	if direct == 1:
        		for i in range(up, down + 1):
        			matrix[i][right] = j
        			j += 1
        		right -= 1
        	if direct == 2:
        		for i in range(right, left - 1, -1):
        			matrix[down][i] = j
        			j += 1
        		down -= 1
        	if direct == 3:
        		for i in range(down, up - 1, -1):
        			matrix[i][left] = j
        			j += 1
        		left += 1
        	if j > n*n:
        	    return matrix
        	direct = (direct + 1) % 4

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        i, j, ii, jj = 0, 0, 0, 1
        for k in range(n*n):
        	matrix[i][j] = k + 1
        	if matrix[(i+ii)%n][(j+jj)%n]:
        		ii, jj = jj, -ii
        	i += ii
        	j += jj
        return matrix

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        low = n*n + 1
        while low > 1:
        	low, high = low - len(matrix), low
        	matrix = [range(low, high)] + zip(*matrix[::-1])
        return matrix

print(Solution().generateMatrix(3))


        