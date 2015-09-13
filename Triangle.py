from Shape import Shape


class Triangle(Shape):
    def __init__(self):
        self.type = "not set"
        self.base = None
        self.height = None

    def get_area(self):
        return (self.base * self.height)/2
