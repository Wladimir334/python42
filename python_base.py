print("Hello world!")


# ТИПЫ ДАННЫХ
# Integer (int) - целые числа
a = 5
b = 6
c = a + b
d = a / b

print(c)
print(d)

# Float (float) - числа с плавающей точкой

float_a = 0.5
float_b = 1.25

print(type(a))
print(type(float_a))

# Boolean - логический тип данных
is_activ = True
is_logout = False

print (is_activ or is_logout)
print (is_activ and is_logout)
print (is_activ and not is_logout)

print(a < b)
print(a > b)
print(a == b)
print(a <= b)
print(a >= b)

# name_of_person - snake case -  змеиный стиль

print(id(a))


# int - приведение строки к типу int
age = "15"
year = "20"
print(int(age) + int(year))

# String (str) - строковый тип данных

text = "I love Python!"

# None


# СТРУКТУРЫ ДАННЫХ
# списки - list() - []

cars = ['bmv', 'audi', True, [1,2]]

# словари - dict() - {}

info = {
    'name': 'Alex',
    'cars': cars,
}

# кортежи - tuple - () - нeизменяемый список
colors = (
    ('red', '255.0.0'),
    ('blue', '0.0.255')
)

# set() - множества - {} - при выводе удаляет все дубликаты

set_numbers = {1,2,3,4,5,5,5} # выведется только 1,2,3,4,5

# функции
# файлы
# классы


#  ввод данных из консоли
name = input("Введите своё имя: ")
age = input("Введите возраст: ")

