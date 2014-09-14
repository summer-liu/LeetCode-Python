class Point:
	def __init__(self, a = 0, b = 0):
		self.x = a 
		self.y = b

class Solution:
	def maxPoints(self,points):
		length = len(points)
		maxP = -1
		if length < 3:
			return 2
		for i in range(length):
			samePointsNum = 1 
			slope = {"infinity": 0}
			for j in range(length):
				if i == j:
					continue
				if (points[i].x == points[j].x) && (points[i].y != points[j].y):
					slope("infinity") += 1 
				elif (points[i].x == points[j].x) && (points[i].y == points[j].y):
					samePointsNum += 1
				else:
					k = 1.0*(points[i].y - points[j].y)/(points[i].x - points[j].x)
					if k in slope:
						slope[k] += 1
					else:
						slope[k] = 1
			maxP = max( maxP, max(slope.value()+samePointsNum))
		return(maxP)


