class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
        	area = max(area, (right-left)*min(height[left], height[right]))
        	if height[left] < height[right]:
        		left += 1
        	elif height[left] > height[right]:
        		right -= 1
        	else:
        		left += 1
        		right -= 1
        return area

s = Solution()
height = [1,4,5,2,3,7,8,9]
print(s.maxArea(height))		