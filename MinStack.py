class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        min =  4 2
        4  2  6  1
        0  -2   -1
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.stack[-1]
        self.stack.pop()
        if top == self.min[-1]:
            self.min.pop()

        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]



class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min  = 0
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack) == 0:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            self.min = min(self.min, x)

        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack) == 0:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min -= pop
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        top = self.stack[-1]
        return self.min + (top if top > 0 else 0)

        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        
