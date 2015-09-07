class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (type(n) != int) or n < 1:
        	raise ValueError('Input value must be positive integer!')
        if n == 1:
        	return 1
        loc2, loc3, loc5 = 0, 0, 0
        uglyList = [1]
        while len(uglyList) < n:
        	v2, v3, v5 = uglyList[loc2]*2, uglyList[loc3]*3, uglyList[loc5]*5
        	next = min(v2, v3, v5)
        	if next == v2:
        		loc2 += 1
        	if next == v3:
        		loc3 += 1
        	if next == v5:
        		loc5 += 1
        	uglyList.append(next)
        return uglyList[-1]

s = Solution()
ans = s.nthUglyNumber(11)
print(ans)


