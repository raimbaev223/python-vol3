# Словари

# dict_with_pairs = {'Ключ1': 'Значение', 'Ключ2': 'Значение2'}
# dict_ = {3: 1, 3.4: 2, 3: 2}
# print(dict_)

# method fromkeys создает новый словарь из переданных ему ключей

# names = {'name1': 'John', 'name2': 'Tom'}
# print(names['name1'])
# print(names['name2'])

# dictionary = dict.fromkeys(['key1', 'key2'])
# print(dictionary)
# dictionary2 = dict.fromkeys(['key1', 'key2'], ['val1', 'val2'])
# print(dictionary2)

# извлечение данных из соваря

# test = {'name': 'John', 'lastname': 'Snow'}
# print(test['name'])
# print(test['lastname'])
# print(test['key'])

# some_dict = {1:5, 2:8, 3:4}
# some_dict[4] = 10 + 5
# # print(some_dict)
# some_dict['key'] = 'value'
# # print(some_dict)
# some_dict['key2'] = [1,2,3,4]
# some_dict['key3'] = {1:1, 2:2}
# # print(some_dict)
# some_dict['key3']['key'] = {3:3, 4:4}
# # print(some_dict)
# some_dict['key3'] = 'значение'
# print(some_dict)
#
# dictionary = {}
# dictionary[1] = 1
# # print(dictionary)
# dictionary['dictionary2'] = {2:2}
# # print(dictionary)
# dictionary['dictionary2'][3] = 3
# print(dictionary)
# print(dictionary['dictionary2'][3])

# method get получает по ключу значение


# cars = {'mersedes': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.get('subaru'))
# print(cars['subaru'])
#
# method keys выводит все ключи

# cars = {'mersedes': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.keys())
# cars_list = cars.keys()
# print(cars_list)
# print(len(cars))
# mersedes = cars.get('mersedes')
# print(mersedes)

# method values выводит все значения
# cars = {'mersedes': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.values())
# print(type(cars.values()))

# method pop вырезает по ключу и возвращает значение нужно указывать ключ в скобках
#
# dict_ = {'first': '1st', 'second': '2nd', 'third': '3rd'}
# print(dict_)
# first = dict_.pop('first')
# print(dict_)
# print(first)


# method popitem вырезает последнееключ и значение

# cars = {'mersedes': '221', 'bmw': '750i', 'subaru': 'impreza'}
#
# deleted = cars.popitem()
# print(cars)

# method update объеденяет 2 словаря в один

# laptops = {'lenovo': 'yoga', 'macbook': 'pro', 'asus': 'zephyrus'}
# laptops2 = {'dell': 'allienware'}
# laptops3 = {'macbook2': 'air'}
# print(laptops)
# laptops.update(laptops2)
# laptops.update(laptops3)
# print(laptops)


# method setdefault сохраняет значение по ключу

# dict_ = {'key1': 1, 'key2': 2, 'key3': 3}
# new_ = dict_.setdefault('key2')
# print(new_)
# new = dict_['key2']
# print(new)
# new2 = dict_.get('key2')
# print(new2)

#
# capitals = dict(Russia = 'Moscow', Kyrgizstan = 'Bishkek', USA = 'Washington')
# print(capitals)
# {'Russia': 'Moscow', 'Kyrgizstan': 'Bishkek', 'USA': 'Washington'}
# capitals = dict([('Russia', 'Moscow'), ('Kyrgizstan', 'Bishkek')])
# print(capitals)
# capitals = {'Russia': 'Moscow', 'Kyrgizstan': 'Bishkek'}
# print(capitals)


# Множество/set

# set_ = [1,2,3,4,5,6,7,1,2,1,2,1]
# print(set_)
# set_ = set(set_)
# print(set_)

# method add  добавляет элемент в множество

# set_ = {1, 2, 3}
# print(set_)
# print(type(set_))
# set_.add(4)
# print(set_)

# method remove удаляет элемент из множества

# set_ = {2,3,5,1,6,9,7,8}
# print(set_)
# #
# set_.remove(1)
# print(set_)

# method discard также как и remove удаляет
#
# set_ = {}
#
# set_.discard(1)
# print(set_)

# method pop вырезает элемент

# set_ = {1,2,3,4,5,6,7,8,9,0}
# print(set_)
# print(set_.pop())


# dict1 = {1:1, 2:2, 3:3}
# dict2 = {4:4, 5:5, 6:6}
# dict_ = dict1 | dict2
# print(dict_)