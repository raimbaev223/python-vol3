# генераторы списков
#
# new_list = [i for i in range(1, 21)]
# print(new_list)
#
# new_list2 = []
# for i in range(1,21):
#     new_list2.append(i)
# print(new_list2)

# new_list_even = [num for num in range(1,21) if num % 2 == 0]
# print(new_list_even)
#
# new_list_odd = [num for num in range(1,21) if num % 2 == 1]
#
# print(new_list_odd)
# анонимная функция лямбда
# lambda_func = lambda x, y: x + y
#
# print(lambda_func(5,5))
#
# print(lambda_func(10,10))

# функция map

# list1 = ['1', '2', '3', '4', '5', '6']
# new_list = list(map(int, list1))
# print(new_list)

# list_ = [x for x in range(1, 51)]
#
#
# def my_func(x):
#     return x * x
#
#
# new_list = list(map(my_func, list_))
# print(new_list)

#
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def my_func(element):
#     element = str(element) + ' element'
#     return element
#
#
# new_tuple = tuple(map(my_func, list_))
#
# print(new_tuple)


# text = 'hello world'
# text2 = list(text)
#
#
# def new_func(a):
#     a = a.upper
#     return a
#
#
# new_text = str(map(new_func, text2))
# print(new_text)

# mixed_list = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
#
# zolushka = list(filter(lambda x : x == 'мак', mixed_list))
#
# print(zolushka)


# def filter_odd_num(in_num):
#     if (in_num % 2) == 0:
#         return True
#     else:
#         return False
#
#
# nums = [ 1, 2, 4, 5, 7, 8, 10, 11]
#
# out_filter = filter(filter_odd_num, nums)
#
# print(list(out_filter))

#
# from functools import reduce
# from datetime import datetime
#
# start1 = datetime.now()
#
# items =[num for num in range(1, 1000001)]
# sum_all = reduce(lambda x, y: x + y, items)
# print(sum_all)
# end1 = datetime.now()
#
# start2 = datetime.now()
#
#
# def lambda_f(x, y):
#     return x + y
#
#
# sum2 = reduce(lambda_f, items)
# print(sum2)
# end2 = datetime.now()
# print(end1 - start1)
# print(end2 - start2)
#
# a = [1, 2, 3]
# b = "xyz"
# c = (None, True, False)
# res = list(zip(a, b, c))
# print(res)

#
# names = ['Erkin', 'Kirill', 'Altynbek']
# ages = [31, 28, 18]
# tel = [12312, 1323123]
# new_dict = dict(zip(names, ages, tel))
# new_tuple = tuple(zip(names, ages, tel))
# new_list = list(zip(names, ages, tel))
# new_set = set(zip(names, ages))
# print(new_dict)
# print(new_tuple)
# print(new_set)
# print(new_list)


# function enumerate
# list_ = [1,2,3,4,5,6,7,8,9,0]
# new_list = []
#
# for num in enumerate(list_):
#     new_list.append(num)

# print(new_list)
# new_list = []
# text = 'hello world'
# for i in enumerate(text):
#     print(i)
#     new_list.append(i)
# print(new_list)

# decorators
# def wrapper_func():
#     def hello():
#         print('hello')
#     hello()
#
# wrapper_func()

# def hello():
#     print('hello')
#
# h = hello()

# def decorator_function(hello_world):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         hello_world()
#         print('Выходим из обёртки')
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world')
#
#
#
# hello_world()

#
# def decorator_func(func):
#     return 'DECORATOR'
#
#
# @decorator_func
# def hello_world():
#     print('hello world')
#
#
# hello_world
#
def burger(func):
    def bur(*args, **kwargs):
        print('Верхняя булочка')
        func(*args, **kwargs)
        print('Нижняя булочка')
    return bur


def kotleta(func):
    def kot(*args, **kwargs):
        print('курочка')
        func(*args, **kwargs)
        print('Говядина')
    return kot


@burger
@kotleta
def nachinka(cheese, tomatoes, cucumber, sous):
    print('\n', cheese, '\n', tomatoes, '\n', cucumber, '\n', sous, '\n', )


nachinka('Сыр','Помидоры','Огурцы', 'Соус')


b = burger(kotleta(nachinka('Сыр','Помидоры','Огурцы', 'Соус')))
b()
