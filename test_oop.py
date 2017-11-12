# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __hash__(self):
#         return hash(self.email)
#
#     def __eq__(self, obdhj):
#         return self.email == obj.email
#
# john = User('John Connor', 'johnconnor@ex.com')
# sonya = User('Sonya Blade', 'johnconnor@ex.com')
# print(john == sonya)
# print(hash(john.email))
# print(hash(sonya.email))
#
# class Researcher:
#     def __getattr__(self, name):
#         return 'Nothing found :('
#
#     def __getattribute__(self, name):
#         print('Looking for {}'.format(name))
#         return 'nope'
#
#
# obj = Researcher()
# print(obj.attr)
# print(obj.method)
# print(obj.DFG2H3J00KLL)
#
# class Ignorant:
#     def __setattr__(self, name, value):
#         print(f"Not gonna set {name}!")
#
#
# obj = Ignorant()
# obj.math = True
#
# print(obj.math)
#
#
# class Polite:
#     def __delattr__(self, name):
#         value = getattr(self, name)
#         print(f'Goodbye  { name }, you were  { value } !')
#         object.__delattr__(self, name)
#
#
# obj = Polite()
# obj.attr = 10
# obj.a = 12312312
# del obj.attr
# del obj.a
#
#
# class Logger:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             with open(self.filename, 'a') as f:
#                 f .write('oh Danny boy...')
#
#             return func(*args, **kwargs)
#         return wrapper
#
# logger = Logger('index.txt')
#
# # itpower1
# import random
#
#
# class NoisyInt:
#     def __init__(self, val):
#         self.val = val
#
#     def __add__(self, obj):
#         noisy = random.uniform(-1, 1)
#         return self.val + obj.val + noisy
#
#
# a = NoisyInt(10)
# b = NoisyInt(20)
# for i in range(10):
#     print(random.uniform(-1, 1))
#
#
# class PascalList:
#     def __init__(self, original_list=None):
#         self.container = original_list or []
#
#     def __getitem__(self, index):
#         return self.container[index - 1]
#
#     def __setitem__(self, index, value):
#         self.container[index - 1] = value
#
#     def __str__(self):
#         return self.container.__str__()

