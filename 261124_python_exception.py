from http.client import responses

import requests

"""
try:
    блок,где возможна ошибка

except:
    действие в случае ошибки

finally:
    блок кода, который выполнится в любом случае
"""
#
#
# age = input('Enter the age: ')
# try:
#     if age < 18:
#         print('error')
#     else:
#         print('ok')
# except:
#     if age.isdigit():
#         if int(age) < 18:
#             print('error')
#         else:
#             print('ok')
#     else:
#         print("not a number")
#
#
# def send_data():
#     data = {'name': 'Alex', 'age': 26}
#     data = None
#     return Exception('ERROR')
#
# def get_data_from_server():
#     try:
#         data = send_data()
#         print(data)
#     except:
#         data = []
#         for i in data:
#             print(i)
#
# try:
#     my_dict = {'name': 'Dima'}
#     if not my_dict.get('age'):
#         raise Exception('нет такого ключа')
#
# except Exception as err:
#     print(err)


# def check_age(age):
#     if age > 100:
#          raise Exception('Возраст слишком большой')
#     return age
#
# try:
#     print(check_age(222))
# except:
#     print('возникла ошибка')

# get_data_from_server()


def get_page(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
    except:
        print('Error')
    print('code')

url = "https://ruuu.wikipedia.org/wiki/Заглавная_страница"
get_page(url)










