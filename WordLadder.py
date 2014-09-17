class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = [(start,1)]
        wordLen = len(start)
        while queue:
            curr = queue.pop(0)
            currWord = curr[0]
            currLen = curr[1]
            for i in range(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != currWord[i]:
                        nextWord = part1 + j + part2
                        if nextWord == end:
                            return currLen+1
                        if nextWord in dict:
                            queue.append((nextWord,currLen+1))
                            dict.remove(nextWord)
        return 0    