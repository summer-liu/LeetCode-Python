class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
    	aLen = len(a)
    	bLen = len(b)
    	if aLen > bLen:
    		b = "0"*(aLen - bLen) + b
    	elif aLen < bLen:
    		a = "0"*(bLen - aLen) + a
    	Len = len(a)
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = ""
        for i in range(Len):
            tmp = int(a[i])+int(b[i])+carry
            res += str(tmp%2)
            carry = tmp/2
        if carry == 1:
            res += "1"
        return res[::-1]








s = Solution()
a = s.addBinary("1010","1011")
print a



class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
    	aDecimal = 0
    	bDecimal = 0
        for i in range(len(a)):
        	aDecimal += int(a[i])*2**(len(a)-1-i)
        	print aDecimal
        for i in range(len(b)):
        	bDecimal += int(b[i])*2**(len(a)-1-i)
        #print aDecimal,bDecimal
        sum = aDecimal + bDecimal
        res = ""
        if sum == 0:
        	return "0"
        quotient = sum
        while quotient != 0:
        	quotient = sum/2
        	mod = sum%2
        	res += str(mod)
        	sum = quotient
        return res[::-1]
