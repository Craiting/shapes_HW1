from Shape import Shape


class Rectangle(Shape):
    def __init__(self, name, height, width):
        self.kind = name
        self.height = height
        self.width = width
        super(Rectangle, self).__init__("Rectangle")

    def get_area(self):
        return self.height * self.width
