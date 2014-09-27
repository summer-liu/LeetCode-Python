class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
    	def fill(x,y):
    		if x < 0 or x >=m or y < 0 or y >= n or board[x][y] != 'O':
    			return
    		queue.append((x,y))
    		board[x][y] = '$'
    	def bfs(x,y):
    		if board[x][y] == 'O':
    			queue.append((x,y))
    			fill(x,y)
    			while queue:
    				curr = queue.pop(0)
    				i = curr[0]
    				j = curr[1]
    				fill(i+1,j)
    				fill(i-1,j)
    				fill(i,j+1)
    				fill(i,j-1)

    	if len(board) == 0:
    		return 
    	m = len(board)
    	n = len(board[0])
    	queue = []     				
    	for i in range(n):
    		bfs(0,i)
    		bfs(m-1,i)
    	for j in range(1,m-1):
    		bfs(j,0)
    		bfs(j,n-1)
    	for i in range(m):
    		for j in range(n):
    			if board[i][j] == '$':
    				board[i][j] = 'O'
    			elif board[i][j] == 'O':
    				board[i][j] = 'X'



        
 

s = Solution()
board = [   ['X','X','X','X'],
 			['X','O','O','X'],
			['X','X','O','X'],
			['X','O','X','X']] 
s.solve(board)
print board