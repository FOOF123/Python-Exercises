import math
class Point:
    def __init__(self, x, y):
        [self.x, self.y] = [x, y]
    def __str__(self):
        return f"({self.x}, {self.y})"
    def distance_from_origin(self):
        return str(math.sqrt(self.x**2 + self.y**2))
    def reflectx(self):
        return Point(-self.x, self.y)
    def reflecty(self):
        return Point(self.x, -self.y)
    def distance(self, point):
        return math.sqrt(abs((self.x - point.x)**2 + (self.y - point.y)**2))
    def slope(self, point):
        try:
            if (self.y - point.y)/(self.x - point.x) == -0.0:
                return 0.0
            return (self.y - point.y)/(self.x - point.x)
        except ZeroDivisionError:
            return ("Undefined Slope - x-coordinates equal")
    def equation_of_line(self,point):
        return (self.slope(point), (self.y-self.slope(point)*self.x))