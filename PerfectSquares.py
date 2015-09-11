class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
        	dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        r =  int(n**0.5) + 1
        for i in range(r):
        	for j in range(i, r):
        		t = i*i + j*j
        		k = 0 if (n-t)<=0 else int((n-t)**0.5)
        		if(n - t - k*k == 0):
        			return 3 - (not i) - (not j) - (not k)
        return 4

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = n
        while m % 4 == 0:
        	m = m >> 2
        if m % 8 == 7:
        	return 4
        r = int(n**0.5)
        if r*r == n:
        	return 1
        else:
        	for i in range(1,r+1):
        		re = n - i*i
        		k = int(re**0.5)
        		if re - k*k == 0:
        			return 2
        return 3

print(Solution().numSquares(1))        