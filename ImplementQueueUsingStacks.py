class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        l = len(self.queue)
        if l == 1:
        	del self.queue[0]
        else:
	        for i in range(1,l):
	        	self.queue[i-1] = self.queue[i]
	        del self.queue[l-1]

	        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0




class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outStack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
        	while self.inStack:
        		self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.inStack) + len(self.outStack) == 0

        