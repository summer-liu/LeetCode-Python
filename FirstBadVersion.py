# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version): 1 2 3  4 5 6 7 8 9 10

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        while lower < upper:
        	mid = lower + (upper - lower)//2
        	if(isBadVersion(mid)):
        		upper = mid
        	else:
        		lower = mid + 1
        return lower