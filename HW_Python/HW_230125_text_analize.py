import json
from collections import Counter
import string

class TextAnalyzer:
    total = {}
    with open(file='poem.txt', mode='r', encoding='utf-8') as file:
        poem = file.read()

    def __init__(self, poem, total):
        self.poem = poem
        self.total = total

    def poem_length(self, poem='my_file.read()'):
        return len(poem)
    result = len(poem)
    length = 'Количество знаков всего: ' + str(result)
    print(length)
    total[length] = {}

    def letters_only(self, poem='my_file.read()'):
        return sum(1 for x in poem if x.isalpha())
    result2 = sum(1 for x in poem if x.isalpha())
    letters = 'Количество только букв: ' + str(result2)
    print(letters)
    total[letters] = {}


    def lines(self, poem='my_file.read()'):
        return len(poem.splitlines())
    result3 = len(poem.splitlines())
    line = 'Количество строк: ' + str(result3)
    print(line)
    total[line] = {}


    def full_lines(self, poem='my_file.read()'):
        return sum(1 for line in poem.splitlines() if line.strip())
    result4 = sum(1 for line in poem.splitlines() if line.strip())
    fulls = 'Количество непустых строк: ' + str(result4)
    print(fulls)
    total[fulls] = {}


    def words(self, poem='my_file.read()'):
        return len(poem.split())
    result5 = len(poem.split())
    wordd = 'Количество слов в тексте: ' + str(result5)
    print(wordd)
    total[wordd] = {}


    def words_per_line(self, poem='my_file.read()'):
        return [len(line.split()) for line in poem.splitlines()]
    result6 = [len(line.split()) for line in poem.splitlines()]
    word_per_l = "Слов в каждой строке:" + str(result6)
    print(word_per_l)
    total[word_per_l] = {}


    def characters_per_line(self, poem='my_file.read()'):
        return [len(line) for line in poem.splitlines()]
    result7 = [len(line) for line in poem.splitlines()]
    characters = "Символов в каждой строке:" + str(result7)
    print(characters)
    total[characters] = {}


    def repeated_words(self, poem='my_file.read()'):
        return Counter(poem.lower().translate(str.maketrans('', '', string.punctuation)).split())
    result8 = Counter(poem.lower().translate(str.maketrans('', '', string.punctuation)).split())
    repeated = "Повторяющиеся слова:" + str(result8)
    print(repeated)
    total[repeated] = {}

    def letter_frequency_analysis(self, poem='my_file.read()'):
        return Counter([char.lower() for char in poem if char.isalpha()])
    result9 = Counter([char.lower() for char in poem if char.isalpha()])
    letter_frequency = "Частотный анализ букв:" + str(result9)
    print(letter_frequency)
    total[letter_frequency] = {}


    def find_non_letter_symbols(self, poem='my_file.read()'):
        return Counter([char for char in poem if not char.isalnum()])
    result10 = Counter([char for char in poem if not char.isalnum()])
    find_non_letter = "Посторонние символы (пробелы и знаки препинания):" + str(result10)
    print(find_non_letter)
    total[find_non_letter] = {}


    total2 = str(total)
    print(total2)


    def write_total(self):
        with open("result.txt", "w") as f:
            f.write(self.total2)



