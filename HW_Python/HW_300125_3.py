

distance = input("Введите дистанцию в метрах: ")
dist = int(distance)
const_tax = int(50)
fare = int(2)


def ride_cost(dist):
    cost = dist / 300 * fare
    return cost

result = round(ride_cost(dist) + const_tax)
result2 = str(result)
print("Стоимость проезда: " + result2 + " руб.")

