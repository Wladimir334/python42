from functools import reduce


def sum(a,b):
    return a + b
result = sum(5, 4)
print(result)

# double = lambda x: x**2
# print(type(double))
# print(double(2))

def double(x):
    return x**2

list_numbers = ['1', '2', '233', '55', '766']

# list_int_numbers = []
# for i in list_numbers:
#     if i.isdigit():
#         list_int_numbers.append(int(i))

# list_int_numbers = list(map(int, list_numbers))
# list_double_numbers = list(map(lambda x: int(x)**2, list_numbers))
#
# print(list_numbers)
# print(list_int_numbers)


sum_numbers = reduce(lambda x,y: int(x) + int(y), list_numbers)
print(sum_numbers)


users = [['alex', 70], ['dima', 50], ['elena', 30], ['elena', 25]]

old_users = list(filter(lambda user: user[-1] > 30, users))

# old_users = []
# for i in users:
#     if i[1] > 30:
#         old_users.append(i)
print(old_users)











