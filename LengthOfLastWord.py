import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = s.strip()
        # if len(s) == 0:
        # 	return 0
        # t = s.split(' ')
        # return len(t[-1])
        return len(s.strip().split(' ')[-1])
        