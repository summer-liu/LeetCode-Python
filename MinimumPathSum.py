class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        mps = [[0 for i in range(n)] for i in range(m)]
        mps[0][0] = grid[0][0]
        for i in range(1,m):
        	mps[i][0] = mps[i-1][0] + grid[i][0]
        for j in range(1, n):
        	mps[0][j] = mps[0][j-1] + grid[0][j]
        for i in range(1, m):
        	for j in range(1, n):
        		mps[i][j] = min(mps[i-1][j], mps[i][j-1]) + grid[i][j]
        return mps[m-1][n-1]

s  = Solution()
grid = [
  [0,8,4],
  [0,1,2],
  [5,2,1]
]
a = s.minPathSum(grid)
print(a)