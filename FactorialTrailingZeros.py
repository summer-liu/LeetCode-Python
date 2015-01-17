class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        d = 1
        r = 0
        while n/(5**d):
            r = r + n/(5**d)
            d += 1
        return r
s = Solution()
a = s.trailingZeroes(101)
print a
            
            
        