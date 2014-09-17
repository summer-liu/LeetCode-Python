class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
    	num.sort()
        n = len(num)
        res = set()
        dict = {}
        if n < 4:
        	return []
        for i in range(n-1):
            for j in range(i+1,n):
                if num[i] + num[j] not in dict:
                    dict[num[i] + num[j]] = [(i,j)]
                else:
                    dict[num[i] + num[j]].append((i,j))
        
        for i in range(n-1):
        	for j in range(i+1,n):
        		t = target - num[i] -num[j]
        		if t in dict:
        			for k in dict[t]:
        				if k[0] > j:
        					res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]
        
 
s = Solution()
A = [1,0,-1,0,-2,2]
target = 0
a = s.fourSum(A,target)
print a