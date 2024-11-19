# условное выражение

age = 14
if age < 20:
    print("Error")
    if age < 15:
        print("Fatal")
    else:
        print("not fatal")
elif age < 25:
    print("<25")
else:
    print("Ok")

print("Next")

# цикл for - цикл счётчиков безусловный цикл

numbers = [1,2,3,4,5,6,7]
cars = ['bmv', 'audi', 'Mercedes']

# for i in numbers:
#     print(i)

# N = 10
# for i in range(1,N+1):
#     print(i)

for ind in range(len(cars)):
    print(ind, cars[ind])

print(cars[1])

a = 10
b = 0
while a < 20:
    print(a)
    b += 1
    if b == 15:
        break
