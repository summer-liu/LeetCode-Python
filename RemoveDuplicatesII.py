class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
		n = len(A)
		if n <= 2:
			return n
		index = 2
		for i in range(2,n):
			if A[i] != A[index-2]:
				A[index] = A[i]
				index += 1


		A = A[:index]
		print A
		return index

s = Solution()
#A = [1,2,3,3,3,3,3,3,3,4,5,5,5,6]
A = [0,1,1,1,2,2,3,3,3,4,5,5,6,6,6,6,7,8,9]
a = s.removeDuplicates(A)
print a