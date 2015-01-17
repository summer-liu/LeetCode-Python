class Solution:
    # @return a string
    def convertToTitle(self, num):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l = len(alpha)
        r = ''
        while num:
        	r = alpha[(num-1)%l] + r
        	num = (num-1)/l
        return r
