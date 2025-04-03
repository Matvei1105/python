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