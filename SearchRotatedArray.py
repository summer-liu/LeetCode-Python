class Solution():
	def search(self, A, target):
		n = len(A)
		first = 0
		last = n
		
		while first < last:
			mid = (first + last)/2
			if A[mid] == target:
				return mid
			if A[first] < A[mid]:
				if A[first] <= target and target < A[mid]:
					last = mid
				else:
					first = mid + 1
			else:
				if A[mid] < target and target <= A[last-1]:
					first = mid + 1
				else:
					last = mid
		return -1


s = Solution()
A = [5,0,1,2,3,4]
target = 4
a = s.search(A,target)
print a