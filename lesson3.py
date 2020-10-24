# LISTS/списки

# method append дополняет список элементами

# list_ = []
# list_.append('world')
# print(list_)
# print(len(list_))
# list_.append('hello')
# print(list_)
# print(len(list_))
# string = ' '.join(list_)
# print(string)
# list_.append(['good', 'bye'])
# print(list_)
# print(len(list_))
# list_.append([123, 234, 456, 789])
# print(list_)

# range создание списков каких то чисел
#
# list_ = list(range(1, 50, 2))
# print(list_)

# method insert получает два аргумента , первый индекс, второй сам элемент

# cars = ['Mersedes', 'Subaru', 'Honda']
# print(len(cars))
# cars.insert(1, 'Toyota')
# print(cars)
# cars.insert(0, 22)
# print(cars)
# list_ = list(range(1, 5))
# cars.insert(2, list_)
# print(cars)
# print(len(cars))
# list_ = []
# list_.append(cars)
# print(list_)
# print(len(list_))
# print(len(cars))

# method remove удаляет элемент по названию

# laptops = ['Lenovo', 'Asus', 'Acer', 'Hp', 'Acer']
# print('before remove', laptops)
# laptops.remove('Acer')
# print('after remove', laptops)

# method pop удаляет и возвращает элемент/ по умолчанию последний

# programming = ['c', 'python', 'js', 'go', 'java']
# print('before', programming)
# last_element = programming.pop(1)
# print('after', programming)
# print(last_element)

# method index возвращает индекс элемента(его номер в списке)

# movies = ['звездные войны', 'джентельмены', 'why him?', 'godfather', '1+1']
# print(movies.index('1+1'))
# number_in_list = movies.index('1+1')
# print(number_in_list)
# print(number_in_list ** number_in_list)
# print(type(number_in_list))

# method count считает количество элементов
#
# list_ = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']
# print(list_.count('blackberry'))
# string = 'hello world'
# print(string.count('l'))
# new_list = list(string)
# print(new_list)
# splited = string.split()
# print(splited)

# method reverse разворачивает список в обратную сторону

# numbers = [1,2,3,4,5,6,7,8,9,0]
# # reversed_numbers = numbers.reverse()
# # print(reversed_numbers)
#
# list_ = [1,2,3,4,5,6]
# print(list_)
# list_.reverse()
# print(list_)
# string = 'hello world'
# simple = string[::-1]
# new = list(string)
# new.reverse()
# new_string = ''.join(new)
# print(new_string)
# print(simple)


# method sort сортирует элементы в списке по ключу


# numbers = [2, 3, 1, 5, 4]
# print(numbers)
# # numbers.sort()
# # print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# list_ = ['John', 'Raychel', 'Deineries', 'Axmed', 'Logan', 'Peter Parker']
# list_.sort()
# # list_.sort(reverse=True)
# print(list_)

# method copy копирует список
#
# list_ = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']
# new_list = list_.copy()
#
# new_list.append('blackberry')
# print(new_list)
# print(list_)

# method extend расширяет список другим списком(складывает)
#
# nums = [1, 2, 3, 1, 2, 3, 4, 5, 6]
# nums2 = [4, 5, 6]
# # nums = nums + nums2
# nums.extend(nums)
# nums += nums2
# print(nums)

# method clear очищает список
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums)
# nums.clear()
# print(nums)
#
# nums = [1,2,3,4,5,6]
# print(nums[::-1])
#
# numbers = (1,2,3,4,5,1,2,3)
# print(numbers.count(4))
# print(numbers.index(3))


# list_ = [1,2,3,4,5,6,7,8,9,0]
# zero = list_.pop(5)
# print(zero)

# cars = ['mers', 'bmw', 'subaru', 'toyota']
# car = cars.pop(2)
# print(cars)
# print(car)