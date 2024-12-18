from collections import Counter
import string


with open('poem.txt', 'r', encoding='utf-8') as file:
    poem_content = file.read()

def words_per_line(text):
    return [len(line.split()) for line in text.splitlines()]

def characters_per_line(text):
    return [len(line) for line in text.splitlines()]

def repeated_words(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return Counter(words)

def letter_frequency_analysis(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return Counter(letters)

def find_non_letter_symbols(text):
    non_letters = [char for char in text if not char.isalnum()]
    return Counter(non_letters)

words_per_line_result = words_per_line(poem_content)
characters_per_line_result = characters_per_line(poem_content)
repeated_words_result = repeated_words(poem_content)
letter_frequency_result = letter_frequency_analysis(poem_content)
non_letter_symbols_result = find_non_letter_symbols(poem_content)

# Вывод результатов
print("Слов в каждой строке:", words_per_line_result)
print("Символов в каждой строке:", characters_per_line_result)
print("Повторяющиеся слова:", repeated_words_result)
print("Частотный анализ букв:", letter_frequency_result)
print("Посторонние символы (пробелы и знаки препинания):", non_letter_symbols_result)