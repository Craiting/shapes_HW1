from Shape import Shape


class Rectangle(Shape):
    def __init__(self):
        self.height = None
        self.width = None

    def get_area(self):
        return self.height * self.width
