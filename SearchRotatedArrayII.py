class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
		n = len(A)
		first = 0
		last = n
		while first < last:
			mid = (first+last)/2
			if A[mid] == target:
				return True
			if A[first] < A[mid]:
				if A[first] <= target and target < A[mid]:
					last = mid
				else:
					first = mid + 1
			elif A[first] > A[mid]:
				if A[mid] < target and target <= A[last-1]:
					first = mid + 1
				else:
					last = mid
			else:
				first += 1
		return False
        

s = Solution()
A = [5,1,3]
target = 3
a = s.search(A,target)
print a