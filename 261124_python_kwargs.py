


def get_info(name, age=34):
    print(name.title())
    print(age)
get_info(name='alex')


a = [1,2,3]
b = [*a, 4,5,6]
print(b)


# def print_scores(name, *scores):
#     print(f"name - {name}")
#     for i in scores:
#         print(i)
#
# print_scores('dima', 24, 26, 28)


# def func(*args, **kwargs)
#     pass                              # это заглушка!


def print_pet_names(*args, **kwargs):
    print(f'Владелец - {args[0]}')
    """
    dog - Tima
    cat - Barsik
    """
    #
    # for key, value in pets.items():
    #     print(f"{key} - {value}")

    for key in kwargs.keys():
            print(f"{key} - {kwargs[key]}")




print_pet_names('Dima', dog='Tima', cat='Barsik')

