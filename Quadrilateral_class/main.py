import point
import Quad

p = point.Point(5, 3)
t = point.Point(0, 3)

print(p, p.distance_from_origin(), p.reflectx(), p.reflecty().reflectx())

print(p.distance(t), p.slope(t), p.equation_of_line(t))

# points must be rounded to 3 decimal places
square = Quad.Quadrilateral(point.Point(0, 0), point.Point(0, 1), point.Point(1, 1), point.Point(1, 0))
rhombus = Quad.Quadrilateral(point.Point(0, 0), point.Point(0, (2**0.5)), point.Point(1, 1+(2**0.5)), point.Point(1, 1))
rectangle = Quad.Quadrilateral(point.Point(0, 0), point.Point(0, 1), point.Point(2, 1), point.Point(2, 0))
parallelogram = Quad.Quadrilateral(point.Point(0, 0), point.Point(1, 1), point.Point(3, 1), point.Point(2, 0))
trapezoid = Quad.Quadrilateral(point.Point(0, 0), point.Point(0, 1), point.Point(1, 1), point.Point(2, 0))
no_shape = Quad.Quadrilateral(point.Point(0, 0), point.Point(0, 3), point.Point(1, 1), point.Point(2, 0))
for i in [no_shape, trapezoid, parallelogram, rectangle, rhombus, square]:
    print(i)
    print(i.shape())