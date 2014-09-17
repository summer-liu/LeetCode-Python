class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 1:
            return 1
        left = 0
        right = x/2+1
        while left <= right:
            mid = (left+right)/2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1
                       
        


s = Solution()
a = s.sqrt(2)
print a
