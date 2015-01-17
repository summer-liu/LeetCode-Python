class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        left = 0
        right = n - 1
        if n == 1:
        	return num[0]

        while left <= right:
        	if num[left] <= num[right]:
    			return num[left]

       		mid = (left + right) / 2
        	if num[left] < num[mid]:
        		left = mid
        	else:
        		right = mid

s = Solution()
 
num = [3,1,2]
a = s.findMin(num) 
print a  	



        

        