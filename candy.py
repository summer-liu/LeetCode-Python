class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candy = [1]*len(ratings)
    	for i in range(1,len(ratings)):
    		if (ratings[i] > ratings[i-1]) and (candy[i] <= candy[i-1]):
    				candy[i] = candy[i-1]+1

    	for i in range(len(ratings)-1,0,-1):
    		if (ratings[i] < ratings[i-1]) and (candy[i] >= candy[i-1]):
    			candy[i-1] = candy[i]+1
    	print candy
    	return sum(candy)


for i in range(1,4,-1):
	print i

s = Solution()
res = s.candy([2,1])
print res

