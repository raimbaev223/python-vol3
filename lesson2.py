# Strings

# method split Делит строку по разделителю на отдельные слова
# tabnine
#
# text = 'Hello,World,Good,Morning'
# print(text.split(','))
# # ['Hello', 'World', 'Good', 'Morning']

# method isdigit проверяет все ли символы в строке цифры/ возвращает ложь или истину

# num = input('Введите число: ')
# print(num.isdigit())


# method isalpha проверяет являются ли символы в строке буквами

# text = input('Input here: ')
# print(text.isalpha())

# method isalnum gпроверяет все ли символы в строке цифры и буквы

# text = input('Input: ')
# print(text.isalnum())

# method replace заменяет часть строки

# string = 'Hello World!'
# print(string.replace('Hello', 'Goodbye'))
# print(string.replace('o', '*', 2))

# method isupper проверяет все ли символы в верхнем регистре

# text = input('Input: ')
# print(text.isupper())

# method islower проверяет все ли символы в нижнем регистре

# text = input('Input: ')
# print(text.islower())

# method isspace проверяет все ли символы пробелы, табы либо переводы строки
#
# text = '\n'
# print(text.isspace())

# method istitle проверяет является ли строка заголовком
#
# text1 = 'hello world'
# text2 = 'Hello World'
# print(text1.istitle())
# print(text2.istitle())

# method lower перевод букв в нижний регистр
#
# text = 'Hello WORLD'
# text2 = text.lower()
# print(text2)
# print(text)

# method upper переводит буквы в верхний регистр
#
# string = 'Hello world'
# print(string.upper())

#method startswith проверяет начинается ли строка с определенных символов

# text = 'Hello world'
# print(text.startswith('h'))

# method endwith проверяет заканчивается ли строка на какие либо символы

# mail = 'example@google.com'
# print(mail.endswith(''))


# method join склеивает строку из разных частей
#
# text = 'hello, my name is Erkin'
# text_splited = text.split()
# print(text_splited)
# text2 = '_'.join(text_splited)
# print(text2)

# method ord выводит номер символа из таблицы ASCII


# print(ord('a'))
# print('A' < 'a')

# method count считает количество символов которые мы передаем в скобках
#
# text = 'hello World'
# print(text.count('Hello'))

# method strip, lstrip, rstrip удаляет пробелы в начале и конце строки

# text = '   hello world   '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# method swapcase меняет регистр на противоположный

#
# text = 'Hello World'
# text2 = 'helLO WoRlD'
# print(text.swapcase())
# print(text2.swapcase())

# Срез строки

# text = input('Input text: ')
# # print(text[5:0:-2])
# if text == text[::-1]:
#     print('Текст читается одинаково')
# else:
#     print('Текст не читается одинаково')
#
# text = 'привет, как дела?'
# print(text[::-1])


# Форматирование строк

# name = input('Введите свое имя: ')
# age = input('ВВедите свой возраст: ')
# print('Вас зовут ' + name + '. Ваш возраст ' + age)
# print(f"Вас зовут {name}. Ваш возраст {age}.")
# print("Hello, %s" % name)
# print('Hello, {}'.format(name))

# text = """
# В языке Питон нет отдельного символьного типа. Символ — это просто строка длины 1.Строка считывается со стандартного вво
# да функцией input().Для двух строк определена операция сложения (конкатенации), также определена операция умножения стр
# оки на число.
# """
#
# print(text)

# text = 'hello \t world'
# print(text)