from geometry.inheritance_geometry import Geometry


class Triangle(Geometry):
    def __init__(self, base, high):
        self.base = base
        self.high = high

    def info(self):
        return f'Calc Area of Triangle with base {self.base} and high {self.high}'

    def get_area(self):
        return self.base * self.high / 2

    def get_around(self):
        return self.base * 3
