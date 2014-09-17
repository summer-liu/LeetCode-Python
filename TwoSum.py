 class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            dict[num[i]] = [i+1] if num[i] not in dict else dict[num[i]] + [i+1]
        for n in num:
            if target - n in dict:
                if n == target - n:
                    if len(dict[n]) == 2:
                        return (dict[n][0],dict[n][1])
                else:
                    return (dict[n][0],dict[target-n][0]) if dict[n][0] < dict[target-n][0] else (dict[target-n][0],dict[n][0])

     
  
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sortnum = sorted(num)
        print num
        index = []
        n = len(num)
        left = 0
        right = n-1
        while left < right:
            if sortnum[left] + sortnum[right] == target:
                for i in range(n):
                    if sortnum[left] == num[i]:
                        index.append(i)
                        break
                for i in range(n-1,-1,-1):
                    if sortnum[right] == num[i]:
                        index.append(i)
                        break
                index.sort()
                break
            elif sortnum[left] + sortnum[right] > target:
                right -= 1
            else:
                left += 1
        return (index[0]+1, index[1]+1)
            
       
                

s = Solution()
numbers = [0,4,4,0]
target = 0

a = s.twoSum(numbers,target)
print a 



"""

        
        
"""