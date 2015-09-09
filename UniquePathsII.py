class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        up = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
        	if obstacleGrid[i][0] == 1:
        		break
        	up[i][0] = 1
        for j in range(n):
        	if obstacleGrid[0][j] == 1:
        		break
        	up[0][j] = 1
        for i in range(1,m):
        	for j in range(1,n):
        		if obstacleGrid[i][j] != 1:
        			up[i][j] = up[i-1][j] + up[i][j-1]
        return up[m-1][n-1]

s = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
a = s.uniquePathsWithObstacles(grid)
print(a)
