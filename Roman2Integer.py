class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {"I":1, "V":5, "X": 10, "L" : 50, "C":100, "D":500, "M":1000}
        s = s[::-1]
        last = None
        answer = 0
        for x in s:
            if last and roman[x] < last:
                answer -= roman[x]*2
            answer += roman[x]
            last = roman[x]
        return answer  
            
        