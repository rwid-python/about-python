from geometry.oop_class import Area
from geometry.oop_triangle import Triangle

print('Object Orintation Program')
s1 = Area(10, 4)
t1 = Area(10, 10)
t2 = Triangle(10, 7)

print(s1.info())
print(s1.info_s())
print(f'Square Area is : {s1.get_area_square()}')
print(t1.info_t())
print(f'Triangle Area is : {t1.get_area_triangle()}')

print(t2.info())
print(f'Triangle SS Area is : {t2.get_area()}')
print(f'Triangle SS Around is : {t2.get_around()}')