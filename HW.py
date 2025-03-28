# Завдання 1: Розширений клас "Тварина" та підкласи

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} каже: {self.sound}")

    def info(self):
        print(f"Це {self.name}. Йому {self.age} років.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Гав-гав")
        self.breed = breed

    def info(self):
        super().info()
        print(f"Порода собаки: {self.breed}")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Мяу")
        self.color = color

    def info(self):
        super().info()
        print(f"Колір кота: {self.color}")

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age, "Чірік-чірік")
        self.can_fly = can_fly

    def info(self):
        super().info()
        ability = "може" if self.can_fly else "не може"
        print(f"Цей птах {ability} літати.")

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age, "Буль-буль")
        self.water_type = water_type

    def info(self):
        super().info()
        print(f"Тип води: {self.water_type}")

class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, "Іго-го")
        self.speed = speed

    def info(self):
        super().info()
        print(f"Швидкість коня: {self.speed} км/год.")

# Тестування класів тварин
dog = Dog("Бобік", 5, "Німецька вівчарка")
cat = Cat("Мурчик", 3, "Чорний")
bird = Bird("Кеша", 2, True)
fish = Fish("Немо", 1, "Солона")
horse = Horse("Буцефал", 7, 45)

dog.info()
dog.make_sound()

cat.info()
cat.make_sound()

bird.info()
bird.make_sound()

fish.info()
fish.make_sound()

horse.info()
horse.make_sound()

# Завдання 2: Розширений клас "ТранспортнийЗасіб" та підкласи

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Транспорт рухається зі швидкістю {self.speed} км/год.")

class Car(Transport):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        print(f"Автомобіль {self.brand} рухається зі швидкістю {self.speed} км/год.")

class Bicycle(Transport):
    def __init__(self, speed, type_bike):
        super().__init__(speed)
        self.type_bike = type_bike

    def move(self):
        print(f"Велосипед типу {self.type_bike} рухається зі швидкістю {self.speed} км/год.")

class Plane(Transport):
    def __init__(self, speed, airline):
        super().__init__(speed)
        self.airline = airline

    def move(self):
        print(f"Літак компанії {self.airline} летить зі швидкістю {self.speed} км/год.")

class Boat(Transport):
    def __init__(self, speed, size):
        super().__init__(speed)
        self.size = size

    def move(self):
        print(f"Корабель розміру {self.size} рухається зі швидкістю {self.speed} км/год.")

class Train(Transport):
    def __init__(self, speed, rail_type):
        super().__init__(speed)
        self.rail_type = rail_type

    def move(self):
        print(f"Поїзд типу {self.rail_type} рухається зі швидкістю {self.speed} км/год.")

class Motorcycle(Transport):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        print(f"Мотоцикл {self.brand} рухається зі швидкістю {self.speed} км/год.")

# Тестування класів транспорту
car = Car(120, "Toyota")
bicycle = Bicycle(25, "Гірський")
plane = Plane(900, "МАУ")
boat = Boat(50, "Великий")
train = Train(100, "Швидкісний")
motorcycle = Motorcycle(150, "Harley-Davidson")

car.move()
bicycle.move()
plane.move()
boat.move()
train.move()
motorcycle.move()