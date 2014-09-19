class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        maxProfitForward = [0] * n 
        maxProfitBackward = [0] * n
        minPrice = prices[0]
        maxPrice = prices[n-1]
        maxProfit = 0

        for i in range(1,n):
        	minPrice = min(minPrice, prices[i])
        	maxProfitForward[i] = max(maxProfitForward[i-1], prices[i] - minPrice)

        for i in range(n-2,-1,-1):
        	maxPrice = max(maxPrice, prices[i])
        	maxProfitBackward[i] = max(maxProfitBackward[i+1], maxPrice - prices[i])

       	maxProfit = maxProfitForward[n-1]
       	for i in range(n):
       		maxProfit = max(maxProfit, maxProfitForward[i]+ maxProfitBackward[i])

       	return maxProfit


s = Solution()

a = s.maxProfit([2,4,3,6])
print a