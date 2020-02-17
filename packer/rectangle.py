class Rectangle:
    def __init__(self, x=None, y=None, width=None, height=None):
        if x is None:
            x = 0
        if y is None:
            y = 0
        if width is None:
            width = 0
        if height is None:
            height = 0
        if width < 0 or height < 0:
            raise Exception("Make sure the width and height are positive.")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

