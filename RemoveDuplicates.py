class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
		n = len(A)
		if n == 0:
			return 0
		index = 0
		for i in range(1,n):
			if A[index] != A[i]:
				index += 1
				A[index] = A[i]
		A = A[:index+1]
		return len(A)


s = Solution()
A = [1,1,1,2,2,3,3,4]
a = s.removeDuplicates(A)
print a