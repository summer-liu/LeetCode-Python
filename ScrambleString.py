class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l2 != l2 or sorted(s1) != sorted(s2):
        	return False
        if s1 == s2:
        	return True
        f = self.isScramble
        for i in range(1, l1):
        	if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]):
        		return True
        	if f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
        		return True
        return False

