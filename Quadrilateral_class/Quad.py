import point
class Quadrilateral:
    def __init__(self, A = point.Point(x=0,y=0), B = point.Point(x=0,y=0), C = point.Point(x=0,y=0), D = point.Point(x=0,y=0)):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
    def __str__(self):
        return " ".join([str(i) for i in (self.A, self.B, self.C, self.D)])
        
    def shape(self):
        l = [self.A, self.B, self.C, self.D]
        slopes = []
        parallelogram = []
        for i in range(len(l)):
            for x in l:
                if l.index(x) > i:
                    if type(l[i].slope(x)) == float:
                        # points must be rounded to 3 decimal places
                        slopes.append(round(l[i].slope(x), 3))
                    else:
                        slopes.append(l[i].slope(x))
        for i in slopes:
            slopes.remove(i)
            if i in slopes:
                parallelogram.append(True)
                while i in slopes:
                    slopes.remove(i)
        if len(parallelogram) > 0:
            if len(parallelogram) > 1:
                d = [l[0].distance(l[i+1]) for i in range(3)]
                d.sort()
                if d[0] != d[1] and d[2] == ((d[0]**2+d[1]**2)**0.5):
                    return "Rectangle"
                if d[0] == d[1] and d[2] != ((d[0]**2+d[1]**2)**0.5):
                    return "Rhombus"
                if d[0] == d[1] and d[2] == ((d[0]**2+d[1]**2)**0.5):
                    return "Square"
                return "Parallelogram"
            return "Trapezoid"
        return "no shape"