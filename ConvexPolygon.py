from Shape import Shape


class ConvexPolygon(Shape):
    def __init__(self):
        if self.type == "rectangle":
            self.sides = 4
