

my_file = open(file='poem.txt', mode='r', encoding='utf-8')
poem = my_file.read()
# print(poem)

def poem_length(poem):
    return len(poem)

result = poem_length(poem)
print('Количество знаков всего: ' + str(result))


def letters_only(poem):
     return sum(1 for x in poem if x.isalpha())

result2 = letters_only(poem)
print('Количество только букв: ' + str(result2))


def lines(poem):
    return len(poem.splitlines())

result3 = lines(poem)
print('Количество строк: ' + str(result3))


def full_lines(poem):
    return sum(1 for line in poem.splitlines() if line.strip())

result4 = full_lines(poem)
print('Количество непустых строк: ' + str(result4))


def words(poem):
    return len(poem.split())

result5 = words(poem)
print('Количество слов в тексте: ' + str(result5))












