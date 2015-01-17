class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 0
        for e in num:
            if count == 0:
                candidate, count = e, 1
            elif candidate == e:
                count += 1
            else:
                count -= 1
        return candidate
       11111
       11100
       11111