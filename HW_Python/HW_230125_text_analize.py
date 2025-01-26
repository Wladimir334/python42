import json

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
    word = 'Количество слов в тексте: ' + str(result5)
    print(word)
    total[word] = {}

    print(str(total))

    def write_total(self):
        with open("result.txt", "w") as f:
            json.dump(self.total, f, indent=2)

