class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A:
            res ^=i
        return res
        
s = Solution()

res = s.singleNumber([2,5,4,2,5])

print res