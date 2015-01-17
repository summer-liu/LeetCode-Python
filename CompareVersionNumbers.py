class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        v1 = [int(n) for n in v1]
        v2 = [int(n) for n in v2]
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                r = 1
                break
            elif v1[i] < v2[i]:
                r = -1
                break
            else:
                r = 0
        if r == 0:
            if len(v1) > len(v2):
                for j in range(i+1,len(v1)):
                    if v1[j] > 0:
                        r = 1
                        break
            elif len(v1) < len(v2):
                for j in range(i+1, len(v2)):
                    if v2[j] > 0:
                        r = -1
                        break
        return r