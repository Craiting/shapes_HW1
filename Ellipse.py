from Shape import Shape
PI = 3.14159265359


class Ellipse(Shape):
    def __init__(self, name, height, width):
        self.kind = name
        self.height = height
        self.width = width
        super(Ellipse, self).__init__("Ellipse")

    def get_area(self):
        return PI * (self.height/2) * (self.width/2)
