class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
    	stack = []
        for i in tokens:
            if i not in ('+','-','*','/'):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b*1.0/a))
        return stack[0]
                
                

    