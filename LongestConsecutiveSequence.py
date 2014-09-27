class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
    	d = {x: False for x in num}
    	maxLen = 1
    	for n in d:
    		if d[n] == False:
	    		Len = 0
	    		curr = n + 1
	    		while curr in d:
	    			d[curr] = True    			
	    			Len += 1
	    			curr += 1

	    		curr = n-1
	    		while curr in d:
	    			d[curr] = True
	    			Len += 1
	    			curr -= 1
	    		maxLen = max(maxLen, Len+1)
	    
        return maxLen


s = Solution()

num = [100,4,200,3,1,2,101,99,103,102,98]

a = s.longestConsecutive(num)

print a
