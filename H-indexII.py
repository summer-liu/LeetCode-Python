class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        left = 0
        right = l-1
        while left <= right:
        	mid = (left + right) >> 1
        	if citations[mid] == l - mid:
        	    return l - mid
        	if citations[mid] >= l - mid:
        		right = mid - 1
        	else:
        		left = mid + 1
        return l - right - 1

