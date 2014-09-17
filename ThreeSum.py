class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        n = len(num)
        num.sort()
        res = []
        target = 0
        for i in range(n-2):
            if i >= 1 and num[i] == num[i-1]:
                continue
            a = num[i]
            left = i+1
            right = n-1
            while left < right:
                b = num[left]
                c = num[right]
                if b + c == target - a:
                    res.append([a,b,c])
                    while left < right:
                        left += 1
                        right -= 1
                        if num[left] != b or num[right] != c:
                            break
                elif num[left] + num[right] < target - num[i]:
                    while left < right:
                        left += 1
                        if num[left] != b:
                            break
                else:
                    while left < right:
                        right -= 1
                        if num[right] != c:
                            break
        return res          


s = Solution()
A = [-1,0,1,2,-1,-4]
a = s.threeSum(A)
print a