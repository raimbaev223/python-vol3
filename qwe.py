LIST / Список
# new_list = []
# empty_list = list()
# some_details = ['a', 'b', [12,12], 'd', (1,2)]

# print(type(new_list))
# print(empty_list)
# print(some_details)
"""
list()
names = ('john', 'Raychel')
print(list(names))
float(12)
int('7')
str(15)
bool(-1)
complex(1)
tuple(12)
list("hello world")
dict(('key', 'value'))
set([1,2,3,4])
"""
"""
diapazon = range(50, 1, -2)   # start end step 
print(type(diapazon))
print(diapazon)
new_generate_list = list(diapazon)
print(new_generate_list)
"""
"""
# method append добавляет в конец списка
some_list = [1,2,3,4,5]
# print(dir(some_list))
some_list.append(6)
some_list.append("Numbers")
print(some_list)
"""
"""
method extend расширяет список другим списком
list1 = ["User1", 'User2', 'User3']
list2 = ['John', 'Raychel', 'Angela', 'Peter']
# list1 += list2
list1.extend(list2)
print(list1)
"""
"""
# method insert   получает два аргумента добавляет по индексно элеменент
cars = ['Mercedes', 'BMW', 'Honda', 'Audi']
print(len(cars))
cars.insert(len(cars), 'Toyota')
print(cars)
"""
"""
# method remove удаляет по элементно
# FIFO
laptops = ['Lenovo', 'Asus', 'Acer','Hp', 'Acer']
print('before', laptops)
laptops.remove('Acer')
print('after', laptops)
"""
"""
#Method pop по умол удаляет последний элемент, также можно по индексно
# Можно сохранить удаленный элемент
programming_languages = ['Python', 'C', 'JavaScript', 'Golang']
print('before', programming_languages)
programming_languages.pop()
programming_languages.pop(1)
python = programming_languages.pop(0)
print(python)
print(programming_languages)
programming_languages.append(python)
print('after', programming_languages)
"""
"""
method index возвращает индекс элемента
movies = ['Интерстеллар', '1+1', '2+1', 'Ирония судьбы или с легким паром']
print(movies.index('1+1', 1, 5)) 
"""
"""
method count возвращает кол-во вхождении объекта
students = ['Шабан', 'Махмуд', 'Тариель', 'Жазгуль', 'Алтынай', 'Махмуд']
print(students.count('John'))
"""
# method reverse разворачивает список
"""list_ = [1,2,3,4,5,6]
print(list_)
list_.reverse()
print(list_)
"""

# method sort сортирует по key
"""
arrays = [1, 5, 9, 2, 3, 8, 4]
print(arrays)
arrays.sort()
print(arrays)
arrays.sort(reverse=True)
print(arrays)

names = ['John', 'Raychel', 'Deineries', 'Axmed', 'Logan', 'Peter Parker']
names.sort(key=len)
print(names)
"""
"""
def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (5, 5)] 
random.sort(key=takeSecond, reverse=True)
print('Sorted list: ', random)

"""
""" method copy
cars = ['honda', 'Audi', 'Mercedes', ['hello', 'world']]
print('List cars', cars)
new_cars = cars.copy()
new_cars[3][0] = 'BMW'
print('New cars list',new_cars)
print('List cars', cars)
new_cars[0] = 'Solaris'
print('New cars list',new_cars)
print('List cars', cars)
"""
# deepcopy
# method deepcopy
"""
import copy
list_ = [1,2,3, [4,5,6]]
print('Original',list_)
new_copy_list = copy.deepcopy(list_)
print('Copy', new_copy_list)
new_copy_list[3][0] = 'Changed'
print('Copy',new_copy_list) 
print('Original', list_)
"""
"""
# method clear() and object del 
lists = ['some', 'and', 'or', 'if']
print(lists)
# lists.clear()
# print(lists)
del lists[0]
print(lists)
# """
# get element with position
# list_ = [1,2,3,4]
# list_[0]

# DICTIONARIES / Словари
"""
list_ = list(range(1, 100))
empty_dict = {}
dict_with_pairs = {'Ключ1': 'Значение', 'Ключ2': 'Значение2'}
some_dict_with_func = dict(instrument='Guitar', car='BMW')
print(type(empty_dict))
print(dict_with_pairs)
print(some_dict_with_func)
dict_with_tuple = dict([('ru', 'Russia'), ('us', 'America'), ('kg', 'Kyrgystan'), ('list',list_)])
print(dict_with_tuple)
"""

some_dict = {3:2, 2:3, 1.5: 2.5, True: False, False: True, (1,2,3): [1,2,3]}
print(some_dict)

# names = {'name': 'John', 'name': 'Raychel'}
# print(names['name'])

