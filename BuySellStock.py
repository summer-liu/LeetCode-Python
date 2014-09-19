class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	n = len(prices)
    	if n < 2:
    		return 0
    	maxprofit = 0
    	minprice = prices[0]
    	for curr in prices:
    		minprice = min(curr,minprice)
    		maxprofit = max(maxprofit, curr - minprice)
    	return maxprofit

class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	n = len(prices)
    	if n == 2:
    		return max(prices[1]-prices[0],0)
    	buy = 0
    	sell = n-1
    	while buy < sell:
    		mid = (buy+sell)/2
    		left = prices[buy:mid]
    		right = prices[mid:sell+1]
    		return max(self.maxProfit(left) , self.maxProfit(right) , max(right) - min(left) )
    	return 0


s = Solution()
a = s.maxProfit([3,2,6,5,0,3])
print a

        