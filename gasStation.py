class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = 0
        res = 0
        for i in range(n):
            if gas[i]+diff < cost[i]:
                res = i+1
                diff = 0
            else:
                diff += gas[i] - cost[i]
        return res
            

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        sum = 0
        total = 0
        n = len(gas)
        k = -1
        for i in range(n):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                k = i
                sum = 0
        return k+1 if total>=0 else -1

            