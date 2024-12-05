# numbers = [-3, 1, 4, -5]
# pos_numbers = []
# for i in numbers:
#     if i > 0:
#         pos_numbers.append(i)
# print(pos_numbers)
#
# # list comprehension
# pos_numbers_2 = [n for n in numbers if n >0]  # [n**2 или  for n in numbers if n >0]
# print(pos_numbers_2)
#
# # int_numbers =
#
# # int_numbers = []
# # for i in range(10):
# #     int_numbers.append(i)
#
# int_numbers = [n for n in range(10) if n % 2 == 0]
# print(int_numbers)

def print_hello(lang: str):
    if lang == 'ru':
        print("Privet")
    elif    lang == 'en':
        print("Hello")
    elif lang == 'ge':
        print("Gutten tag")
    else:
        print('error')

print_hello(lang="en")

def print_hello_match(lang: str):
    match lang:
        case 'ru':
            print("Privet")
        case 'en':
            print("Hello")
        case "ge":
            print("Gutten tag")
        case _:
            print("error")

print_hello_match(lang='ge')

def print_main_menu():
    print("выберете необходимое действие:")
    print("1. Посмотреть список книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    action = input('>>> ')

    match action:
        case '1': book_list()
        case '2': book_add()
        case '3': book_delete()
        case 'exit':
            print('До свидания')
            exit()
        case _: print('Введите цифру от 1 до 3 или exit для выхода')

def book_list():
    print('список книг')
    action = input('>>> ')

def book_add():
    print('введите название и автора книги:')
    action = input('>>> ')

def book_delete():
    print('введите ID книги для удаления:')
    action = input('>>> ')

print_main_menu()