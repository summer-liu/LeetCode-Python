class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        n = len(s)
        A = [None] * n
        i = n-1
        while i >= 0:
            if s[i:n] in dict:
                A[i] = [n]  # A[i] contains "n" means s[i..n-1] is a word
            else:
                A[i] = []
            # Check al possible j break
            for j in range(i+1, n):
                if A[j] and s[i:j] in dict:
                    A[i].append(j)
            i -= 1
        print A
        res = []  # possible sentences with break
        path_list = [[0]]  # initially, there is only one path containing the source node
        while path_list:
            new_list = []
            # For each path,
            # 1) If the path ends with break "n", then segment the string with breaks of the path
            # 2) otherwise, expand it with all possible breaks
            for path in path_list:
            	#print path
                if path[-1] == n:  # segment!
                    # Get words according to the breaks
                    temp = [ s[path[i]:path[i+1]] for i in range(len(path)-1) ]
                    # join words together
                    res.append(" ".join(temp))
                else:  # expand the path
                    for j in A[path[-1]]:
                    	print path+[j]
                        new_list.append(path+[j])
            print new_list
            path_list = new_list
        	#print path_list
        return res
        

s = Solution()
a = s.wordBreak("catsanddog",["cat","cats","and","sand","dog"])
print a
