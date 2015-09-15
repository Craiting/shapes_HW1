from Shape import Shape


class Triangle(Shape):
    def __init__(self, tri_type, angles, base, height):
        self.kind = tri_type
        self.angles = angles
        self.base = base
        self.height = height
        super(Triangle, self).__init__("Triangle")

    def get_area(self):
        return (self.base * self.height)/2
