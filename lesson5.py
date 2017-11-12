# number = int(input('введите число: '))
# if number > 10:
#     print(f'Вы ввели число {number}, оно больше 10')
# else:
#     print(f'вы ввели число {number}, оно меньше 10')

# number = int(input('введите число: '))

# if number < 0:
#     print(f'число {number} отрицательное ')
# elif number > 0:
#     print(f'число {number} положительное')
# else:
#     print(f'число {number} равно нулю')

# < меньше
# > больше
# <= меньше или равно
# >= больше или равно
# == равняется ли
# != не равно
# or = или
# and = и
# not = не
# num = int(input('введите число: '))
# if num <= 10:
#     print(num)
# else:
#     print('число больше 10')


# num = int(input('введите число: '))
#
# if num < 10 and num > 5:
#     print(f'число {num} больше 5 и меньше 10')
# else:
#     print('условие не верно')

# if num < 10 or num == 100:
#     print(f'число {num} меньше 10 или равно 100')
# else:
#     print('условие не выполнено')


# num1 = int(input('введите первое число: '))
# operator = input('введите оператор +,-,/,*: ')
# num2 = int(input('введите второе число: '))
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '/':
#     print(num1 / num2)
# elif operator == '*':
#     print(num1 * num2)
# else:
#     print('Я вас не понял, запустите код заново')


# text = 'Я вас не понял, запустите код заново'
#
# if 'Я' in text or '123' or 'пока' and 'код':
#     print('условие истинно')
# else:
#     print('условие ложно')

# while бесконечный цикл, выполняется пока условие истинно

# while True:
#     num1 = int(input('введите первое число: '))
#     operator = input('введите оператор +,-,/,*: ')
#     num2 = int(input('введите второе число: '))
#     if operator == '+':
#         print(num1 + num2)
#     elif operator == '-':
#         print(num1 - num2)
#     elif operator == '/':
#         print(num1 / num2)
#     elif operator == '*':
#         print(num1 * num2)
#     else:
#         print('Я вас не понял, запустите код заново')


# i = 0
# while i <= 1000:
#     print(i)
#     i += 1
# i = 0
# while True:
#     print(i ** 1000000)
#     i += 1

# цикл for

# list_ = []
# for num in range(1, 101):
#     list_.append(num)
#     print(num)
# print(list_)

# string = 'Hello, how are you?'
# print(type(string))
# print(string)
# string = string.split()
# print(type(string))
# print(string)
# for letter in string:
#     print(letter.upper())

# summ = 0
# for num in range(1, 101):
#     summ += num
#     print(summ)
# print(summ)


# continue Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
#
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i * 2)
#
# for i in range(1, 21):
#     if i == 10:
#         continue
#     print(i)

# Оператор break досрочно прерывает цикл

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i)

# for i in range(1, 21):
#     if i == 10:
#         break
#     print(i)
#
# print('hello')

# list_ = []
# for num in range(1, 21):
#     list_.append(num)
#     print(list_)


# nums = [i for i in range(1, 21)]
# print(nums)

# A = [0] * 10
# print(A)
# i = 1
# 1 / 2 = 0
# 1
# i = 2
# 2 // 2 = 1
# 0

# from datetime import datetime
# start1 = datetime.now()
# nums = [i for i in range(1, 20000001)]
# # print(nums)
# end1 = datetime.now()
# total1 = end1 - start1
# print(total1)
#
# start2 = datetime.now()
# nums2 = []
# for i in range(1, 20000001 ):
#     nums2.append(i)
# # print(nums2)
# end2 = datetime.now()
# total2 = end2 - start2
# print(total2)


# list_ = (i ** 2 for i in range(1,11))
# print(list_)

# list_ = [input() for i in range(int(input()))]
# print(list_)
# первое число которое вводим, это диапазон, далее мы вводим то что добавить в список
# list2 = []
# for i in range()


# list_ = [i ** 2 for i in range( 11)]
# print(list_)
#
# nums = []
# for number in range(11):
#     number = number ** 2
#     nums.append(number)
# print(nums)

# i = int(input())
# if i < 0:
#     if i == - 5:
#         print('i == -5')
#     print('i < 0')
# list_ = []
# list2 = []
# for i in range(1,21):
#     list_.append(i)
#     print(list_)
#
# for i in list_:
#     i = i * 2
#     list2.append(i)
# print(list2)

# text = 'Вот так можно получить список, заполненный случайными числами от 1 до 9(используя функцию randint из модуля random)'
# string = input('Input here: ')
#
# while True:
#     if string not in text:
#         print('Совпадения не найдены')
#     elif string in text:
#         print(f'слово {string} есть в тексте')
#     elif string == 'stop':
#         break
#
# print("цикл остановлен")


# my_list = [1,2,4,5]
# for i in my_list:
#     if i == 3:
#         print('item found')
#         break
#     print(i)
# else:
#     print('item not found')
#     if i == 3:
#         print('item found')
#         break
#     print(i)
# else:
#     print('item not found')


# while True:
#     num = input('input num: ')
#     print(f'вы ввели {num}')
#     if num == 'stop':
#         print('сработал оператор break')
#         break
# print('код выполняется далее')

# while True:
#     num = input('input num: ')
#     print(f'вы ввели {num}')
#     if num == 'stop':
#         print('сработал оператор continue')
#         continue
#     print('continue не работает')
# print('код выполняется далее')