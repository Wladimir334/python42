from os.path import split

number = 123

def calculate(number):

    a, b, c = map(int, str(number))

    sum = a + b + c
    mult = a * b * c

    return sum, mult


sum, mult = calculate(number)
print(f"Сумма цифр = {sum}, Произведение цифр = {mult}")


# -----------------------------------------------

a = 4
b = 20
x = 10

def interval(a, b, x):
    min_int = min(a,b)
    max_int = max(a,b)
    return min_int < x < max_int

if interval(a, b, x):
    print(f'Number {x} in interval {min(a,b)}, {max(a,b)}')
else:
    print(f'Number {x} not in interval {min(a,b)}, {max(a,b)}')

# ------------------------------------------------

text1 = 'abcde'
text2 = '12345'

def dict(text1, text2):
    return {key: value for key, value in zip(text1, text2)}

result1 = dict(text1, text2)
print(result1)

# -------------------------------------------------

def user(full_name, age, phone):

    if age < 1 or age > 150:
        print("Возраст должен быть от 1 до 150 лет.")
        age = 0


    if not (4 < len(phone) < 11):
        print("Некорректный номер телефона.")
        phone = "8-000-000-00-00"


    user_data = {
        "ФИО": full_name,
        "Возраст": age,
        "Номер телефона": phone,
    }

    return user_data


full_name = input("Введите ваше ФИО: ")

age = int(input("Введите ваш возраст: "))

phone = input("Введите ваш номер телефона: ")


user_info = user(full_name, age, phone)


print("Обработанные данные:")
for key, value in user_info.items():
    print(f"{key}: {value}")

#----------------------------------------------

str = 'Python is the best programming language'

print(len(str))
print(str[0])
print(str[-1])
print(str.split()[0])
print(str.split()[-1])
slice_word = str[19:31]
print(slice_word)

#---------------------------------------------------
def calculator(operation: str, a: float, b: float) -> float:

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b


result2 = calculator('add', 2, 5)
print(f"Результат: {result2}")