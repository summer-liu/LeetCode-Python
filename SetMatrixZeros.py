class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
        	return 
        n = len(matrix[0])
        if n == 0:
        	return 
        zeroRow = ()
        zeroCol = ()
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			zeroRow.add(i)
        			zeroCol.add(j)
        for i in range(m):
        	for j in range(n):
        		if i in zeroRow or j in zeroCol:
        			matrix[i][j] = 0
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
        	return 
        n = len(matrix[0])
        if n == 0:
        	return 
        col0 = 1
        for i in range(m):
        	if matrix[i][0] == 0:
        		col0 = 0
        	for j in range(1, n):
        		if matrix[i][j] == 0:
        			matrix[i][0] = 0
        			matrix[0][j] = 0

        for i in range(m-1, -1, -1):
        	for j in range(n-1, 0, -1):
        		if matrix[i][0] == 0 or matrix[0][j] == 0:
        			matrix[i][j] = 0
        	if col0 == 0:
        		matrix[i][0] = 0
        