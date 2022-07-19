class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist(self, other):
        res = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return res
