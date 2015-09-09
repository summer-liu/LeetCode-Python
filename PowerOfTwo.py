class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and  (n & (n - 1)) == 0
s = Solution()
print(s.isPowerOfTwo(1))        