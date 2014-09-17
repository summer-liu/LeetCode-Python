class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
		n = len(A)
		mid = n/2
		res = []
		if n == 0:
			return [-1,-1]
		if n == 1:
			if A[0] == target:
				return [0,0]
			else:
				return [-1,-1]

		if A[mid] == target:
			left =self.searchRange(A[:mid],target)[0]
			res = [  mid if left == -1 else left, self.searchRange(A[mid:],target)[1]+mid]
			return res
		if A[mid] > target:
			res = self.searchRange(A[:mid],target)
			return res
		if A[mid] < target:
			left = self.searchRange(A[mid:],target)[0]
			right = self.searchRange(A[mid:],target)[1]
			res = [left if left == -1 else (left+mid), right if right == -1 else (right+mid)]
			return res

		return [-1,-1]        
s = Solution()
A=[5,7,7,7,7,7,8,8,10]
target = 7
a = s.searchrange(A,target)
print a