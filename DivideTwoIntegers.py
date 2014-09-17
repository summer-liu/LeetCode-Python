class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        sum = 0
        count = 0
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            sum = divisor
            count = 1
            while sum + sum <= dividend:
                sum += sum
                count += count
            dividend -= sum
            quotient += count
        return quotient*sign


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                quotient += 1<<k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return quotient*sign

s = Solution() 
a = s.divide(-7,3)
print a 

"""


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):       
        if divisor == 0:
            return False
        if dividend == 0:
            return 0
        a = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            dividend = abs(dividend)
            divisor = abs(divisor)
            while dividend >= divisor:
                a += 1
                dividend -= divisor
        else:
            dividend = abs(dividend)
            divisor = abs(divisor)
            while dividend > 0:
                a -= 1
                dividend -= divisor 
        return a
"""        
