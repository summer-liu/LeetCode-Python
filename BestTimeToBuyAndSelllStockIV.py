class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
        	return 0
        if k >= n//2:
        	return self.quick(prices)
        # localMax = [[0 for i in range(k+1)] for j in range(n)]
        # globalMax = [[0 for i in range(k+1)] for j in range(n)]
        # for i in range(1, n):
        # 	diff = prices[i] - prices[i-1]
        # 	for j in range(1, k+1):
        # 		localMax[i][j] = max(globalMax[i-1][j-1] + max(diff, 0), localMax[i-1][j] + diff)
        # 		globalMax[i][j] = max(globalMax[i-1][j], localMax[i][j])
        # return globalMax[n-1][k]
        localMax = [0] * (k+1)
        globalMax = [0] * (k+1)
        for i in range(1, n):
        	diff = prices[i] - prices[i-1]
        	for j in range(k, 0, -1):
        		localMax[j] = max(globalMax[j-1] + max(diff, 0), localMax[j] + diff)
        		globalMax[j] = max(globalMax[j], localMax[j])
        return globalMax[k]



    def quick(self, prices):
    	print('iii')
    	maxProfit = 0
    	for i in range(1, len(prices)):
    		if prices[i] > prices[i-1]:
    			maxProfit += prices[i] - prices[i-1]
    	return maxProfit

    		 
p = [1,4,2,5,7,5,3,6,2,8]
print(Solution().maxProfit(2, p))