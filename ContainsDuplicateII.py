class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        1 3 4 2 3 1
        """
        table = {}
        for i in range(len(nums)):
        	if nums[i] in table:
        		if len(table[nums[i]]) == 1:
        			table[nums[i]].append(i)
        		else:
        			if i - table[nums[i]][1] < table[nums[i]][1] - table[nums[i]][0]:
        				table[nums[i]] = [table[nums[i]][1], i]
        	else:
        		table[nums[i]] = [i]
        for n in table:
        	if len(table[n]) == 2 and table[n][1] - table[n][0] <= k:
        		return True
        return False

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        for i in range(len(nums)):
        	if i > k:
        		window.remove(nums[i-k-1])
        	if nums[i] in window:
        		return True
        	window.add(nums[i])
        return False

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i in range(len(nums)):
        	if nums[i] in table:
        		j = table[nums[i]]
        		if i - j <= k:
        			return True
        	table[nums[i]] = i
        return False
