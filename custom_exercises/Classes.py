class Rectangle:
    """This is the constructor for a rectangle
    it takes for arguments where x1/y1 is the
    lower left corner and x2/y2 is the upper
    right corner. It also defines width and
    height
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1

    def Area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height

    def contains_point(self, x1, y1):
        """
        Returns true if point x1/y1 is within the rectangle, false otherwise
        """
        return (self.x1 <= x1 and x1 <= self.x2) and (self.y1 <= y1 and y1 <= self.y2)


# Create a new rectangle. __init__ will be called (you can check
# this with the debugger)
r = Rectangle(0, 0, 2, 3)


# Print the area of the rectangle
print(r.Area())


# Check if a point is inside the rectangle
if r.contains_point(1, 1):
    print("Point is inside rectangle")
