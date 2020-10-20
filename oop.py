from geometry.oop_class import Area

print('Object Orintation Program')
s1 = Area(10, 4)
t1 = Area(10, 10)

print(s1.info())
print(s1.info_s())
print(f'Square Area is : {s1.get_area_square()}')
print(t1.info_t())
print(f'Triangle Area is : {t1.get_area_triangle()}')

