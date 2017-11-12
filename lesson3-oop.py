# class List:
#     name = 'default'
#     contact = 'default'
#     address = 'default'
#
#     def set_(self, name, contact, address):
#         self.name = name
#         self.contact = contact
#         self.address = address
#
# Kirill = List()
# Kirill.set_('Kirill', '0555555555', '8-ый мкрн')
# k = Kirill = (Kirill.name, Kirill.contact, Kirill.address)
#
# Erkin = List()
# Erkin.set_('Erkin', '0755966065', 'Военно-Антоновка')
# e = Erkin = (Erkin.name, Erkin.contact, Erkin.address)
#
#
# class ContactList(List):
#     name = 'Erkin'
#
#     def search_by_name(self, name):
#         self.name = 1
#
# all_contacts = [Kirill, Erkin]
# all_contacts = ContactList()
# all_contacts.search_by_name(1)
# #
# # for i in range(0, 2):
# #     all_contacts.name = input('input name: ')
# #
# #     if all_contacts.name == 'Kirill':
# #         print(k)
# #
# #     if all_contacts.name == 'Erkin':
# #         print(e)
# for i in range(0, 2):
#     all_contacts.name = input('input name: ')
#     if all_contacts.name in e:
#         print(e)
#     if all_contacts.name in k:
#         print(k)


class House:
    def __init__(self, S):
        self.S = S
    def some_method(self):
        pass
class Furniture(House):
    def abc(self, locker, table, bed):
        self.locker = locker
        self.table = table
        self.bed = bed


s = int(input('Площадь помещения: '))
table = int(input('Площадь стола: '))
locker = int(input('Площадь шкафа: '))
bed = int(input('Площадь кровати: '))
a = Furniture(s)
a.abc(locker, table, bed)
print(f'Площадь квартиры {a.S},\n список мебели внутри: кровать, стол, шкаф')

abc = (a.S - (a.locker + a.bed + a.table))

if abc > 0:
    print(f"Осталось всего {abc} кв.м.")
else:
    print("места для мебели нет")






print(hash(john.email))
print(hash(sonya.email))





