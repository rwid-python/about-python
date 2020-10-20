class Area():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def info(self):
        return f'Formulation with class to count Area of Geometry'

    def info_t(self):
        return f'Area of Triangle with base : {self.v1} and high : {self.v2} :'

    def info_s(self):
        return f'Area of Square with length : {self.v1} and width : {self.v2} :'

    def get_area_square(self):
        return self.v1 * self.v2

    def get_area_triangle(self):
        return self.v1 * self.v2 / 2

