# # # import os, sys, math # так делать не надо
# #
# # import os
# # import sys
# # import math
# # from subprocess import Popen, PIPE
# #
# # import requests
# #
# # from lesson8 import burger
# # # from lesson7 import *  # так делать не стоит
# # import lesson7
# # a = ''
# #
# #
# # def func_1():
# #     pass
# #
# #
# # tuple_ = (
# #     '1-value',
# #     '2-value',
# #     '3-value',
# #     '4-value',
# #     '5-value',
# #     '6-value',
# #     '7-value',
# #     '8-value',
# #     '9-value',
# # )
# #
# #
# # my_list = [
# #     1, 2, 3,
# #     4, 5, 6,
# # ]
# #
# # names = { 'name1' : 'John' , 'name2': 'Tom', 'name3': 'Alice' }
# #
# # x = 1 + 2
# #
# #
# # def func_(x, y):
# #     return x + y
# #
# #
# # func_(1, 2)
# #
# # names['name4'] = 'Erkin'
# #
# # # функция которая складывает 2 числа
# #
# #
# # def add(x, y=10):
# #     return x - y
# #
# # goroda = []
# #
# # imena = []
# #
# #
# # class MyFirstClass():
# #     pass
# #
# #
# # class User:
# #     pass
# #
# #
# # def my_function():
# #     pass
# #
# #
# # PI = 3.14
# #
# # my_var = ''
# #
# #
# # if my_var == True: # не правильно
# #     pass
# #
# #
# # if my_var is True: # правильно
# #     pass
# #
# #
#
# #
# # import math
# #
# # print(math.pi)
# #
# # PI = math.pi
# #
# # print(math.ceil(PI)) # окрушление вверх
# # print(math.floor(PI)) # округление вниз
# #
# # num = -10.111
# #
# # print(abs(num)) # abs возвращает положительное число
# #
# #
#
# import random
#
# # print(random.randint(1, 100)) # вазвращает случайное число в выбранном диапазоне
#
# # print(random.random()) # возвращает случайное дробное число от 0 до 1.0
#
# # print(random.uniform(0, 10)) # возвращает случайное дробное число в выбранном диапазоне
#
# # list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # list1 = []
# # print(random.choice(list_)) # возвращает случайный элемент из итерируемого объекта
#
# # random.shuffle(list_) # перемешивает итерируемый объект
#
# # print(list_)
#
#
# # Модуль  statistics содержит функции для осуществления статистических операций.
# # import statistics
# #
# # list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # result = int(sum(list_) / len(list_))
# #
# #
# # print(statistics.mean(list_))
# # print(result)
#
#
# import datetime     #Классы для работы с датой/временем
# import time         # Функции для работы с временем
# import calendar     # Классы для работы с календарем
# # import pytz       # Данные о всех временных зонах согласно  базе данных часовых поясов
#
#
# # print(datetime.datetime.now())
# # time.sleep(2)
# # print(datetime.datetime.now())
# # years = [2015, 2016, 2017, 2018, 2019, 2020]
# # month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # days = [i for i in range(1, 31)]
# # # print(datetime.date(2020, 11, 2))
# #
# # print(datetime.date(years[0], month[0], days[0]))
#
#
# # print(datetime.datetime.today())
# # print(datetime.datetime.utcnow())
#
# import sys          # Переменные и функции, которые используются/взаимодействуют с интерпретатором
# import platform     # Низкоуровневая информация о платформе
# import os           # способ доступа к системным функциям для разных платформ
# import shutil       # Высокоуровневые операции с файлами (копирование, удаление и др.)
# import subprocess   # Запуск процессов, присоединение к потокам их ввода/вывода и получение кодов возврата
#
#
# # print(platform.machine())   # Возвращает тип машины, например, ' i386'.
# # print(platform.node())      # Возвращает сетевое имя машины.
# # print(platform.processor()) # Возвращает наименование процессора
# # print(platform.system())    # Возвращает название операционной системы
# # print(platform.version())   # Возвращает версию операционной системы
# # print(platform.uname())     # Возвращает именованный кортеж из результатов вызова функций: ( system(), node(), release(), version(), machine(), processor())
#
# # print(sys.maxsize)      # Наибольшее целое число, поддерживаемое ОС.
# #
# # print(sys.platform)     # Строка, содержащая идентификатор платформы.
# #
# # os.startfile('/Users/er.py/test.txt')
# # os.mkdir('new_folder')
# # shutil.copy('test.txt', 'new_folder')
# # print(os.path.getsize('venv'))
#
#
# import random
# comb = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-'
# tech21 = 16
# p = ''.join(random.sample(comb, 20))
# print(p)
# print(len(p))