class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        l = len(citations)
        for i in range(l):
        	if citations[i] >= l - i:
        		return l - i
        return 0

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        count = [0] * (l + 1)
        for c in citations:
        	if c > l:
        		count[l] += 1
        	else:
        		count[c] += 1
        t = 0
        for i in range(l, -1 , -1):
        	t += count[i]
        	if t >= i:
        		return i
        return 0
