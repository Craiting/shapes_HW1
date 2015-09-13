from Shape import Shape
PI = 3.14159265359


class Ellipse(Shape):
    def __init__(self):
        self.height = 0
        self.width = 0

    def get_area(self):
        return PI * (self.height/2) * (self.width/2)
