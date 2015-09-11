class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-k)
        self.reverse(nums, n-k, n)
        self.reverse(nums, 0, n)
    def reverse(self, nums, start, end):
    	for i in range(start, start + (end-start)//2):
    		nums[i], nums[start+end-i-1] = nums[start+end-i-1] , nums[i]

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums,3)
print(nums)
    		# nums[i], nums[start+end-i-1] = nums[start+end-i-1] , nums[i] 


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
         
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b, a%b)
         
        n = len(nums)
        for i in range(gcd(n,k)):
            pre = nums[i]
            j = i
            while (j+k)%n != i:
                nums[(j+k)%n], pre = pre, nums[(j+k)%n]
                j = (j+k)%n
            nums[(j+k)%n] = pre
         
          