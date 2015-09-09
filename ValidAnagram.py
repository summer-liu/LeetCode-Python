class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # table = {}
        # for i in s:
        # 	if i in table:
        # 		table[i] += 1
        # 	else:
        # 		table[i] = 1
        # for i in t:
        # 	if i in table:
        # 		table[i] -= 1
        # 	else:
        # 		return False
        # for k in table:
        # 	if table[k] != 0:
        # 		return False
        # return True
        alphabet = [0] * 26
        for i in s:
        	alphabet[ord(i) - ord('a')] += 1
        for i in t:
        	alphabet[ord(i) - ord('a')] -= 1
        for i in alphabet:
        	if i != 0:
        		return False
        return True

ss = Solution()
s = 'ansagram'
t = 'nagaram'
print(ss.isAnagram(s,t))        
