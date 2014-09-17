class Solution:
	def traprainwater(self,A):
		max = 0
		water = 0
		left  = 0
		right = 0
		for i in range(len(A)):
			if A[i]>A[max]:
				max = i

		for i in range(max):
			if(A[i]>left):
				left = A[i]
			else:
				water += left - A[i]

		for i in range(len(A)-1, max-1, -1):
			if (A[i] > right):
				right = A[i]
			else:
				water += right - A[i]
		return water


	def traprainwater2(self,A):
		n = len(A)
		max_left = [0]*n
		max_right = [0]*n
		for i in range(1,n):
			max_left[i] = max(max_left[i-1],A[i-1])
			max_right[n-i-1] = max(max_right[n-i],A[n-i])

		water = 0
		for i in range(len(A)):
			h = min(max_left[i],max_right[i])
			if h > A[i]:
				water += h-A[i]
		return water



s = Solution()
m = [0,1,0,2,1,0,1,3,2,1,2,1]
a = s.traprainwater(m)
print a