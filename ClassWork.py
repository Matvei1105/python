#Поліморфізм
# class Animal:
#     def sound(self):
#         pass #пустой код
#
# class Dog(Animal):
#     def sound(self):
#         return "ГАВ"
#
# class Cat(Animal):
#     def sound(self):
#         return "МЯУ"
#
# class Cow(Animal):
#     def sound(self):
#         return "МУ"
#
# a1=Dog
# a2=Cat
# a3=Cow
# speak(a1)
# speak(a2)
# speak(a3)

# class Pay:
#     def process(self,money):
#         pass
# class Credit(Pay):
#     def process(self,money):
#         return "Оплата " + str(money) + "грн здійснена через кредитну картку"
# class Cash(Pay):
#     def process(self,money):
#         return "Оплата " + str(money) + "грн здійснена через готівку"
# class System(Pay):
#     def process(self,money):
#         return "Оплата " + str(money) + "грн здійснена через онлайн систему"
# buy=[Credit(),Cash(),System()]
# num=int(input('Введіть суму покупки: '))
# for k in buy
#     print(k.process(num))

# #Інкапсуляція
# #Модифікація Доступу
# #1) Public
# class Dog:
#     def __init__(self,name):
#         self.name=name
# dog1=Dog("Бані")
# print(dog1.name)
#
# #2) Private
# class Dog:
#     def __init__(self,name):
#         self.name=name
#         self.__age=2
#     def info(self):
#         return self.__age
# dog1=Dog("Бані")
# print(dog1.info())
#
# #3) Protected
# #2) Private
# class Dog:
#     def __init__(self,name):
#         self._breed="бульдог"
# class D (Dog):
#     def info(self):
#         return "Це щеня породи "+self._bread
# dog1=D("Бані")
# print(dog1.info())

# class Person:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self._age=age
#         self.__salary=salary
#     def info(self):
#         print("Вітаю! Мене звати",self.name)
#         self._infoAge()
#         self.__infoSalary()
#     def _infoAge(self):
#         print('Мій вік', self._age)
#     def _infoSalary(self):
#         print('Моя ЗП', self.__salary)
# class Employee(Person):
#     def __init__(self,name,age,salary)
#          super().__init__(name,age,salary)
#          self.pos=pos
#     def printInfo(self):
#         print('Моя посада', self.pos)
#         print('Мій вік', self._age)
#         print('Моя ЗП', self.__salary)
# human=Person('Олеся', 20, 2000)
# emp=Employee('Петро', 25, 45000, 'інженер')
# print(human.name)
# human.info()
# print(emp.name)
# emp.printInfo()
# print(emp._age)
# print(emp.__salary)

import random

class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = max(0, health)

    def info_name(self):
        return self.__name

    def info_hp(self):
        return self.__health

    def attack(self):
        pass

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return f"{self.__name} має {self.__health} здоров'я"

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120)

    def attack(self):
        return random.randint(10, 25)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100)

    def attack(self):
        return random.randint(5, 35)

class Slime(Character):
    def __init__(self):
        super().__init__("Слайм", health=random.randint(80, 120))

    def attack(self):
        return random.randint(5, 35)

player = random.choice([Warrior("Воїн"), Mage("Маг")])
slime = Slime()

print(f"{player.info_name()} вступает в битву с {slime.info_name()}!")

while player.is_alive() and slime.is_alive():
    damage_to_slime = player.attack()
    slime.take_damage(damage_to_slime)
    print(f"{slime.info_name()} получил {damage_to_slime} урона! {slime}")

    if slime.is_alive():
        damage_to_player = slime.attack()
        player.take_damage(damage_to_player)
        print(f"{player.info_name()} получил {damage_to_player} урона! {player}")

if player.is_alive():
    print(f"{player.info_name()} победил!")
else:
    print(f"{slime.info_name()} победил!")