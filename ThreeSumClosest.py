class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
		n = len(num)
		if n < 3:
			return None
		sum = 0
		min_diff = 1000
		num.sort()
		for i in range(n-2):
			j= i+1
			k = n-1
			while j<k:
				sum = num[i] + num[k] +num[j]
				diff = abs(sum-target)
				if diff < min_diff:
					min_diff = diff
					i0,j0,k0 = i,j,k
				if sum > target:
					k -= 1
				else:
					j +=1
		return num[i0]+num[j0]+num[k0]








s = Solution()
numbers = [0,0,0]
target = 1

a = s.threeSumClosest(numbers,target)
print a