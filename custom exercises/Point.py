class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)


p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = p1 + p2

print(p3)
