class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
		m = len(matrix)
		n = len(matrix[0])
		first = 0
		last = m*n
		while first < last:
			mid = first + (last-first)/2
			val = matrix[mid/n][mid%n]
			if target == val:
				return True
			elif target > val:
				first = mid +1
			else:
				last = mid
		return False


s = Solution()
matrix = [
			[1,3,5,7],
			[10,11,16,20],
			[23,30,34,50]
			]
target  = 16

a = s.searchMatrix(matrix,target)
print a