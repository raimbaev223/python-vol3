# class Dog():
#     def __init__(self, size, name):
#         self.size = size
#         self.name = name
#
#     def speak(self):
#         if self.size == 'small':
#             print("Это маленькая собака")
#         elif self.size == 'middle':
#             print("Это средняя собака")
#         elif self.size == "large":
#             print("это большая собака")
#
#
# class Doberman(Dog):
#     def __init__(self, name, size="large"):
#         self.name = name
#         self.size = size
#
#     def speak(self):
#         print("Это собака породы доберман")
#
#
# rex = Doberman('Rex')
# rex.speak()
# bobik = Dog('middle', 'Bobik')
# bobik.speak()

#
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Появился новый питомец. Отработал метод init')
#
#     def talk(self):
#         print('....')
#
# class Fish(Pet):
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#         print('появилась новая рыбка. Отработал метод init')
#
#
# class Cat(Pet):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         print('Появился кот. Отработал метод init')
#
#     def talk(self):
#         print('Мяу')
#
# class Turtle(Pet):
#     def run(self, x, y):
#         self.x = x
#         self.y = y
#         print(f'Черепаха пробежала расстояние {self.x + self.y} метра')
#
# class Dog(Pet):
#     def __init__(self, name, age, breed, size='large'):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.size = size
#         print('Появился пес. Отработал метод init')
#
#     def speak(self):
#         if self.size == 'little' or self.size == 'medium':
#             print('gav')
#         elif self.size == 'large':
#             print('Woof')
#
# dori = Fish("dori", 1, 'blue')
# dori.talk()
# rex = Dog('Rex', 3, 'doberman')
# gray = Dog('gray', 2, 'dachshund', 'little')
# sam = Cat('sam', 4, 'mainkun')
# donotello = Turtle('donotello', 5)
# donotello.run(1, 2)
# rex.speak()
# gray.talk()
#
# sam.talk()



# class Animal:
#     def __init__(self, name, hunger=6):
#         self.name = name
#         self.hunger = hunger
#
#     def eat(self, food=1):
#         self.hunger += food
#         print('animal eating')
#
#     def status(self):
#         print(f"hunger of {self.name}: {self.hunger}")
#
#
# class Cat(Animal):
#     def meow(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('meow')
#         else:
#             print(f'{self.name} hunger = {self.hunger}')
#
# class Dog(Animal):
#     def bark(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('woof')
#         else:
#             print(f'{self.name} hunger = {self.hunger}')
#
# cat = Cat('cat', 3)
# cat.meow()
# dog = Dog('dog')
# dog.status()
# dog.bark()
# dog.status()
# cat.status()
# cat.eat(4)
# cat.status()
# cat.meow()


# class Animals:
#     def __init__(self, name):
#         self.name = name
#
#     def breathe(self):
#         print('дышит')
#
#     def move(self):
#         print('двигается')
#
#     def eat_food(self):
#         print('ест')
#
# class Mammals(Animals):
#     def feed_young_with_milk(self):
#         print('кормят детенышей молоком')
#
# class Giraffes(Mammals):
#     def eat_leaves_from_trees(self):
#         print('едят листья с деревьев')
#
#     def move(self):
#         print('жираф передвигается')
#
# melman = Giraffes('Melman')
# melman.breathe()
# melman.feed_young_with_milk()
# melman.eat_food()
# melman.eat_leaves_from_trees()
# melman.move()