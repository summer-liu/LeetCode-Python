class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):       
		n = len(A)
		mid = n/2
		if n == 1:
			if A[0] == target:
				return 0
			elif A[0] > target:
				return 0
			else:
				return 1

		if A[mid] == target:
			return mid
		elif A[mid] > target:
			return self.searchInsert(A[:mid],target)
		else:
			return self.searchInsert(A[mid:],target)+mid




s = Solution()
A = [1,3,5,6,8,9,12]
target = 15
a = s.searchInsert(A,target)
print a