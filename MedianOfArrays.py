class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):       
		m = len(A)
		n = len(B)
		total = m + n
		if total&0x1:
			return self.find_kth(A,m,B,n,total/2+1)
		else:
			return (self.find_kth(A,m,B,n,total/2)+ self.find_kth(A,m,B,n,total/2+1))/2.0

	def find_kth(self,A,m,B,n,k):
		if m > n:
			return self.find_kth(B,n,A,m,k)
		if m == 0:
			return B[k-1]
		if k == 1:
			return min(A[0],B[0])

		ia = min(k/2,m)
		ib = k - ia
		if A[ia-1] < B[ib-1]:
			return self.find_kth(A[ia:],m-ia,B,n,k-ia)
		elif A[ia-1] > B[ib-1]:
			return self.find_kth(A,m,B[ib:],n-ib,k-ib)
		else:
			return A[ia-1]




s = Solution()
A = [2,4,5,6]
B = [1,3,5,7,8]

a = s.findMedianSortedArrays(A,B)
print a