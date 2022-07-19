class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist(self, other):
        res = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return res

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square(self):
        pi = 3.14
        s = pi * self.radius**2
        return s

    def do_intersect(self, other):
        dis = self.center.dist(other.center)
        if dis <= self.radius + other.radius:
            return True
        else:
            return False