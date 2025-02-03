

def count_dict(input_string):
    char_count = {}

    for char in input_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    unique_count = len(char_count)
    return unique_count


input_string = input("Введите строку: ")
unique_char_count = count_dict(input_string)
print(f"Количество уникальных символов (словарь): {unique_char_count}")


def count_set(input_string):
    unique_chars = set(input_string)

    unique_count = len(unique_chars)
    return unique_count


input_string = input("Введите строку: ")
unique_char_count = count_set(input_string)
print(f"Количество уникальных символов (множество): {unique_char_count}")
