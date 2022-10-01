class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overwrite the + operator so now you can add points
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    # overwrite the - operator so you can subtract points
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    # implement __str__ function for convenience
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)


p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = p1 + p2

print(p3)
