class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def connect(self,begin,end,words,L,l, is_last):
        res = ""
        tmp = words[begin:end+1]
        print tmp[0]
        num = end - begin
        #print num
        if is_last:
            t0 = " ".join(tmp) if num>1 else tmp[0]
            res = t0 + " "*(L-len(t0))
            return res
        if num == 0:
            res = " "*L
            return res
        if num == 1:
            res=tmp[0]+" "*(L-l)
            return res
        else:
            l1 = (L-l)%num
            l2 = (L-l)/num 
            t = []
            if l1 == 0:
                res= (" "*l2).join(tmp)
            else:
                for j in range(len(tmp)):
                    if l1:
                        t += tmp[j] + " "*(l2+1)
                        l1 -= 1
                    elif j != len(tmp)-1:
                        t += tmp[j] + " "*l2
                    else:
                        t += tmp[j]             
                        res = "".join(t)
        #print len(res)
        return res

    def fullJustify(self, words, L):
        n = len(words)
        print n
        begin = 0
        l = 0
        res = []
        if L == 0:
            return [""]
        if n == 0:
            return [" "*L]
        for i in range(n):
            if ( l + len(words[i]) + (i - begin) > L ):
                res.append(self.connect(begin, i-1, words,L,l, False ))
                begin = i
                l = 0
            l += len(words[i])
        print res
        res.append(self.connect(begin, n-1, words, L, l , True))
        return res






s = Solution()

words = ["This", "is", "ann", "example", "of", "text", "justification."]
#words = ["hello","world."]
words = ["What","must","be","shall","be."]
L = 12
words = [""]
L = 0
a = s.fullJustify(words,L)

print a


"""
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        length = len(words)
        res = []
        tmp = []
        l = 0
        i = 0
        end = False
        for w in words:
            if l+len(w)+i <= L:
                l += len(w)
                tmp.append(w)
                i += 1
                if w.__contains__("."):
                    end = True
            else:
                break
        print tmp

        if end:
            t0 = " ".join(tmp)
            t1 = t0 + " "*(L-len(t0))
            return res.append(t1)

        if i == 1:
            res.append(tmp[0]+" "*(L-l))
        else:
            l1 = (L-l)%(i-1) 
            l2 = (L-l)/(i-1) 
            t = []

            if l1 == 0:
                res.append((" "*l2).join(tmp))
            else:
                for j in range(len(tmp)):
                    if l1:
                        t += tmp[j] + " "*(l2+1)
                        l1 -= 1
                    elif j != len(tmp)-1:
                        t += tmp[j] + " "*l2
                    else:
                        t += tmp[j]             
                res.append("".join(t))  
            #print self.res
        if words[i:]:
            return res.append(self.fullJustify(words[i:],L))
"""
        