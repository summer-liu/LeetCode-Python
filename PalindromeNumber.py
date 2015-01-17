# import math
# class Solution:
#     # @return a boolean
#     def isPalindrome(self, x):
#         if x < 0:
#             return False
#         if x < 10:
#         	return True
#        	digits = int(math.log10(x)) + 1
#         for i in range(digits/2):
#         	lowest = x / (10**i) % 10
#         	highest = x / (10**(digits-i-1)) % 10
#         	if lowest != highest:
#         		return False
#         return True
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
            
        while x:
            left = x / div
            right = x % 10
            print left, right
            
            if left != right:
                return False
            
            x = ( x % div ) / 10
            print x
            div = div / 100
        return True
s = Solution()
a = s.isPalindrome(123454321)
print a
        
        