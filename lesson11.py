# 1
# i = 0
# while i < 11:
#     i += 1
#     print(i)

# 2
# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 1:
#         print(i)

# 3
#
# num = int(input('Input number: '))
# #i = 7
# x = 1
# while num != 7:
#     print('Попробуйте еще')
#     num = int(input('Input number: '))
#     x += 1
# else:
#     print('ok')


# 4

# password = 123
# q = 0
# while q < 3:
#     pass1 = int(input('Input password: '))
#     q +=1
#     if pass1 == password:
#         print('OK')
#         break
# else:
#     print('Vy potratily vse popytky')


#5

# a = int(input("a: "))
# b = int(input("b: " ))
# c = int(input("c: " ))
# g = [i for i in range(a, b+1)]
# k = []
# for i in g :
#     if i % c == 0:
#         print(k.append(i))
# print(k)
# print(len(k))
#
#



#6


# num = int(input('write the num: '))
# while num != 0:
#     num -= 1
#     print('+'*(num+1))


# list_ = ['aktilek', 'kana', 'roza', 'nazar']
# while True:
#     user = input('uchenik')
#     if user == "exit":
#         break
#     else:
#         list_.append(user)
# print(list_)

# 8

# a = int(input('input: '))
# b = 0 if a % 2 == 0 else 1
# while b <= a:
#     print(b)
#     b += 2


# 9
#
# a = int(input(': '))
# step = 1
# while 2 ** step <= a:
#     print(2**step)
#     step += 1

# word = 'like'
# word1 = list(word)
# life = 5
# while 0 <= life:
#     a = input('Введите слово: ')
#     if a in word1:
#         b = (word1.index(a)+1)
#         print(f'Это {b} ')
#     else:
#         life -= 1
#         print(f'У вас осталось {life} жизней')

# word = 'like'
# list_word = list(word)
# input_list = []
# c = len(word)
# while True:
#     b = input('Введите букву: ')
#     if b in word:
#         print("Буква имеет позицию:", (word.find(b) + 1))
#         if b not in input_list:
#             input_list.append(b)
#             if len(list_word) == len(input_list):
#                 print('вы выиграли!')
#                 break
#     elif b not in word:
#         c -= 1
#         print('не правильно! Количество оставшихся попыток: ', c)
#         if c == 0:
#             print('попытки закончились!')
#             break
#
# word = 'like'
# c = len(word)
# while c > 0:
#     b = input('Введите букву: ')
#     if b in word:
#         print('Буква имеет позицию:',word.find(b))
#     else:
#         c -= 1
#         print('Не правильно:',c)
# print('Попытки закончились!')