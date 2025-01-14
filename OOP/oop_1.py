"""
    ООП

     Класс - общее описание предметной области на языке программирования
     Объект - экземпляр (конкретный представитель)
     Метод - функция свзанная с объектом класса (классом)
     Атрибут - характеристика (свойство) объекта или класса (это какбы переменные)
     Конструктор - метод, который управляет созданием объекта

     Инкапсуляция - механизм позволяющий скрывать внутренние детали реализации объекта и предоставлять доступ к ним,
     только, через определённые методы, чтобы защитить данные и кониролировать доступ к ним.
"""

# class Car:
    # атрибуты класса
    # brand = "BMW"
    # color = "Black"

    # метод объекта
    # def go(self):
    #     print("Car drive")

# создание экземпляра (объекта) класса Car
# car = Car()
# car_2 = Car()
# print(car.brand, car.color)
# car.go()
# print(Car.brand, Car.color)
# print(car_2.brand, car_2.color)
#
#
# car_3 = Car(brand="Audi", model="A6", year=2024, power=249)

class Car:
    _COLORS = ("red", "green", "blue", "")
    def __init__(self, brand, model, year, power, currency="RUB"):
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.country = "USA"    # указанный  параметр и все объекты будут его иметь по умолчанию
        self.currency = currency
        self.is_power = False

        # защищённые атрибут (нижнее подчёркивание перед именем)
        self._color = ""

        # приветный атрибут (два нижних подчёркивания перед именем)
        self.__speed = 100

    def go(self):
        if self.is_power:
            print(f"{self.brand} {self.model} to go!")
        else:
            print("Car must be power on!")

    def stop(self):
        if self.is_power:
            print(f"{self.brand} {self.model} stop!")
        else:
            print("Car must be power on!")

    def turn(self, direction):
        if self.is_power:
            print(f"{self.brand} {self.model} TURN {direction.upper()}")
        else:
            print("Car must be power on!")

    def power_on(self):
        if self.is_power:
            print("Car is already power on!")
        else:
            print(f"{self.brand} {self.model} power on!")
            self.is_power = True


    def power_off(self):
        if not self.is_power:
            print("Car is already power off!")
        else:
            print(f"{self.brand} {self.model} power off!")
            self.is_power = False

    def display_color(self):
        print(self._color)

    def set_color(self, new_color):
        if new_color in Car._COLORS:
            self._color = new_color
        else:
            raise ValueError("Неправильный цвет")


car_audi = Car(brand="Audi", model="A6", year=2024, power=249)
car_bmw = Car(brand="BMW", model="X7", year=2024, power=500)

# car_audi.go()
# car_bmw.go()
#
# print(car_audi.country)
# print(car_bmw.currency)
#
# car_bmw.turn(direction="left")
# car_bmw.turn(direction="right")
#
# car_bmw.engine = "d"
# print(car_bmw.engine)
#
# car_bmw.power_on()
# car_bmw.power_on()
# car_bmw.power_off()
# car_bmw.turn()


car_audi.power_off()
car_audi.go()
car_bmw.turn(direction="right")
car_audi.power_on()
car_audi.power_on()
car_audi.go()
car_bmw.turn(direction="right")
car_audi.power_off()
car_audi.power_off()

# car_audi._color = "green"
# print(car_audi._color)

# print(car_audi.__speed)

print(car_audi._Car__speed)