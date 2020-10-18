# Tutorial use function from package
from geometry.area import calc_triangle, calc_square, calc_round, calc_rectangle

high = 10
base = 4
diameter = 7
length = 5
width = 3

print(f"Calculate area Triangle  = {calc_triangle(base, high)}")
print(f"Calculate area Square  = {calc_square(length)}")
print(f"Calculate area Round  = {calc_round(diameter)}")
print(f"Calculate area Rectangle  = {calc_rectangle(length, width)}")
