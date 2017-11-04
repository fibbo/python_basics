class Rectangle():
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.width = x2 - x1
		self.height = y2 - y1

	def Area(self):
		return self.width*self.height

	def contains_point(self, x1, y1):
		return (self.x1 <= x1 and x1 <= self.x2) and (self.y1 <= y1 and y1 <= self.y2)



r = Rectangle(0,0, 2, 3)


print(r.Area())

if r.contains_point(1,1):
	print("Point is inside rectangle")