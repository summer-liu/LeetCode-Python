class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        h = m*[n*[0]]
        h[m-1][n-1] = max(0, -dungeon[m-1][n-1]) + 1;
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1 , -1):
                down = None
                if i + 1 < m:
                    down = max(1, h[i+1][j] - dungeon[i][j])
                right = None
                if j + 1 < n:
                    right = max(1, h[i][j+1] - dungeon[i][j])
                if down and right:
                    h[i][j] = min(down, right)
                elif down:
                    h[i][j] = down
                elif right:
                    h[i][j] = right
        return h[0][0]



s = Solution()
d = [[100]]
dd = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
a = s.calculateMinimumHP(dd)
print a






