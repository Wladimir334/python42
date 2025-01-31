import random


def min_max(numbers: list) -> tuple:
    if not numbers:
        raise ValueError("The list must not be empty!")

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers[1:]:
      if num < min_num:
          min_num = num
      if num > max_num:
          max_num = num

    return min_num, max_num

random_numbers = [random.randint(0, 100) for _ in range(10)]
print(f"Generated numbers: {random_numbers}")

min_value, max_value = min_max(random_numbers)
print(f"Minimum number: {min_value}, Maximum number: {max_value}")


