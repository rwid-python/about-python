#About Data Type in Python with Data List or Array
#List of Child use scalar data (data sederhana)
child1 = 'Eko'
child2 = 'Dwi'
child3 = 'Tri'
print(child1)
print(child2)
print(child3)
#Example use Data Array
array_child = ['Eko','Dwi','Tri']
print(f'Hai my son : {array_child} !')
array_child.append('Catur')
array_child.append('Ponco')

#SHOW DATA INDEX ARRAY
print(f'Hai My Son #2 {array_child[1]}')

#SHOW ALL DATA
i = 1
for a in array_child:
    print(f'Hai My Son #{i} : {a}')
    i = i+1

#SHOW LIST WITH RANGE (START, END)
for b in range(3,len(array_child)):
    print(f'{b+1}. Hai My Son : {array_child[b]}')

