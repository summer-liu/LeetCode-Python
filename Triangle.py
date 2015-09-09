class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        mps = triangle[n-1]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                mps[j] = min(mps[j], mps[j+1]) + triangle[i][j]
        return mps[0]

s = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(triangle))        	
