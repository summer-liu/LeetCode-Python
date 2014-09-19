class Solution:
    # @return an integer
    def reverse(self, x):
        sign = 1 if x > 0 else -1
        string = str(abs(x))
        res = string[::-1]
        return sign*int(res)
        
        