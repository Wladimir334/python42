

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
print('Количество слов: ' + str(result5))


def words_in_line(poem):
    return [len(line.split()) for line in poem.splitlines()]

result6 = words_in_line(poem)
print('Количество слов в строке: ' + str(result6))

from collections import Counter
import re

words_in_poem = re.findall(r'\r\w+\r', poem.lower())

word_count = Counter(words_in_poem)

repeated_words = {word: count for word, count in word_count.items if count > 1}
sorted_words = dict(sorted(repeated_words.items, key=lambda item: item[1], reverse=True))

for word, count in sorted_words.items:
    print(f'{word}: {count}')





