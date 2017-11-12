# def hello():
#     print('hello')
#
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # c = int(input('Введите третье число: '))
# # list_ = [a, b, c]
# # if a > b and a > c:
# #     while True:
# #         m = a
# #         print(m)
# #         break
# # m = a
# # if m < b:
# #     while True:
# #         m = b
# #         print(m)
# #         break
# #     m = b
# # else:
# #     m = a
# # if m < c:
# #     while True:
# #         m = c
# #         print(m)
# #         break
# #     m = c
# # else:
# #     m = b
# print('hello')
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # c = int(input('Введите третье число: '))
# # m = a
# # if m < b:
# #     m = b
# # if m < c:
# #     m = c
# # print(m)
#
# # l = [1,2,3]
# # l = tuple(l)
# print('hello')
# # num = int(input('Число: '))
# # step = int(input('Степень: '))
# # if num < 100:
# #     result = num ** step
# #     print('Результат: ', result)
# # else:
# #     print('Число >= 100')
# #
# # num1 = int(input('Введите первое число: '))
# # num2 = int(input('Введите второе число: '))
# # num3 = int(input('Введите третье число: '))
# # if num1 > num2 and num1 < num3:
# #     print('первое число среднее')
# # elif num2 > num1 and num2 < num3:
# #     print('второе число среднее')
# # else:
# print('hello')
# # n = int(input('Введите количество яблок в корзине: '))
# # x = int(input('Введите количество студентов: '))
# # if n > x:
# #     print(f'Каждый студент получил по {n // x} яблок' + ' ' + f'остаток в корзине {n % x}')
# # if x > n:
# #     ost = n - n // x
# #     print(f'Студентов {x}, яблок в корзине {n}, остаток яблок в корзине {ost}')
#
#
# # def add(q,w,e,r,t,y,u,i,o,p):
# #     return q + w + e + r + t + y + u + i + o + p
# #
# # print(add(1,2,3,4,5,6,7,8,9,10))
# #
# #
# # def add(*args):
# #     result = 0
# #     for num in args:
# #         result = result + num
# #     return result
# #
# # print(add(1,2,3,45,))
#
#
# # def func(a=10, b=20, c=30):
# #     return a + b + c
# #
# # print(func(1,2))
#
# hello()
# # def myfunc(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210):
# #     print(f'{Firstname}, \n{Lastname}, \n{Email}, \n{Country}, \n{Age}, \n{Phone}')
# #
# #
# # # myfunc(Lastname='Snow')
# #
# # dict_ = dict(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# #
# # def myfunc2(**kwargs):
# #     for key, value in dict_.items():
# #         print(f"{key}: {value}")
# #
# # myfunc2()
#
# def many(*nums, **names):
#     print(nums)
#     print(names)
#
#
# # many(1, 2, 3,4,5,6, name="Mike", job="programmer", mail='example@domain.com', phone='123123123')
#
#
#
# hello()
import time
import sys
# def short_story():
#     print("У попа была собака, он ее любил.")
#     print("Она съела кусок мяса, он ее убил,")
#     print("В землю закопал и надпись написал:")
#     # time.sleep(1)
#     short_story()
#
#
# short_story()


def factorial(n):
    sys.setrecursionlimit(10000)
    # if n == 1:
    #     return 1
    # else:
    # time.sleep(1)
    # print(n)
    print(f"{n} * factorial({n} - 1)")
    return n * factorial(n - 1)


print(factorial(2))
