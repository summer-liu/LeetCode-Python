class MinStack:
    # @param x, an integer
    # @return an integer
    a = []
    def push(self, x):
    	a.append(x)
    	return x


    # @return nothing
    def pop(self):
    	a.pop()
        

    # @return an integer
    def top(self):
    	return a[len(a)-1]
        

    # @return an integer
    def getMin(self):
    	
        