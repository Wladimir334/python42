

class TextAnalyzer:
    my_file = open(file='poem.txt', mode='r', encoding='utf-8')
    poem = my_file.read()
    def __init__(self,my_file):
        self.my_file = my_file


    def read_file(self, my_file):
        my_file = open(file='poem.txt', mode='r', encoding='utf-8')

        print(read.my_file)


    def lines(self):
        pass


    def symbols(self):
        pass
        # return sum(1 for x in poem if x.isalpha())


    def words(self):
        pass


    def write_to_file(self):
        pass


read = TextAnalyzer(my_file = open(file='poem.txt', mode='r', encoding='utf-8'))

read.read_file()