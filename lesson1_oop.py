# class MyClass:
#     pass
#

# class Person():
#     pass
#
#
# Person.money = 150
#
# obj1 = Person()
# obj2 = Person()
# obj1.name = 'Bob'
# obj2.name = 'Masha'
# print(obj1.name, 'has', obj1.money, 'dollars')
# print(obj2.name, 'has', obj1.money, 'dollars')

# class Person:
#     name = ''
#     money = 0
#
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj1.money = 200
# obj2.name = 'Masha'
#
# print(obj1.name, 'has', obj1.money, 'dollars')
# print(obj2.name, 'has', obj2.money, 'dollars')


# class Person:
#     name = ''
#     money = 0
#
#     def out(self): # self - это ссылка на экземпляр класса
#         print(self.name, 'has', self.money, 'dollars')
#
#     def change_money(self, new_money):
#         self.money = new_money
#
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj2.name = 'Masha'
#
# obj1.out()
# obj2.out()
#
# obj1.change_money(180)
# obj1.out()


# class Pet():
#     """Виртуальный питомец"""
#
#     def __init__(self, name): # метод-конструктор, срабатывает при создании нового объекта
#         print('Появилось новое животное класса Pet')
#         self.name = name
#
#     def __str__(self): # возвращает строку, которая содержит значение атрибута name
#         rep = 'Объект класса Pet\n'
#         rep += 'имя: ' + self.name + '\n'
#         return rep
#
#     def talk(self):
#         print(f'Привет, я экземпляр класса Pet, мое имя {self.name}\n')
#
# pet1 = Pet('Bobik')
# pet1.talk()
# pet2 = Pet('Sharik')
# pet2.talk()
# print(pet1)
# print(pet2)

# class Pet():
#     total = 0
#
#     @staticmethod
#     def status():
#         print(f"\nВсего животных сейчас {Pet.total}")
#
#     def __init__(self, name):
#         self.name = name
#         print('Появилось новое животное класса Pet')
#         Pet.total += 1
#
#
# print(Pet.total)
#
# pet1 = Pet('Bobik')
# pet2 = Pet('Murzik')
# pet3 = Pet('Sharik')
#
# Pet.status()

# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).

# class A:
#     def _private(self):
#         print('This is private method')
#
#
# a = A()
# a._private()
#
# class B:
#     def __private(self):
#         print('Это закрытый метод')
#
# b = B()
# # b.__private()
# b._B__private()


# class Pet():
#     def __init__(self, name, mood):
#         print('Появилось новое животное')
#         self.name = name
#         self.__mood = mood
#
#     def talk(self):
#         print('меня зовут', self.name)
#         print('Сейчас я чувствую себя', self.__mood, '\n')
#
#     def __private_method(self):
#         print('Это закрытый метод')
#
#     def public_method(self):
#         print('Это открытый метод')
#         self.__private_method()
#
# pet = Pet(name='Бобик', mood='Отлично')
#
# pet.talk()
# pet.public_method()


class Pet:
    # конструктор класса, инициализирует 3 открытых атрибута
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    # закрытый метод, увеличивающий чувство голода и скуки
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    # свойство, отражает самочувствие животного
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'так себе'
        else:
            m = 'ужасно'
        return m

    # метод сообщает о самочувствии животного
    def talk(self):
        print('Меня зовут', self.name)
        print('И сейчас я чувствую себя', self.mood)

    # метод снижает уровень голода животного
    def eat(self, food=4):
        print('Спасибо')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    # метод снижает уровень уныния животного
    def play(self, fun=4):
        print('Урааа')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    pet_name = input('Как вы назовете свое животное: ')
    pet = Pet(pet_name)
    choice = None
    while choice != '0':
        print(
            """
            Мой питомец
            0 - выйти
            1 - узнать о самочувствии
            2 - покормить животное
            3 - поиграть с животным
            """
        )
        choice= input('Ваш выбор: ')
        if choice == '0':
            print('До свидания!')
        elif choice == '1':
            pet.talk()
        elif choice == '2':
            pet.eat()
        elif choice == '3':
            pet.play()
        else:
            print('Извините, в меню нет такого пункта', choice)

main()
input('Нажмите ENTER для выхода')