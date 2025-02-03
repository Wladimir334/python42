

poem_text = """Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.
В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.
Шли годы. Бурь порыв мятежный
Рассеял прежние мечты,
И я забыл твой голос нежный,
Твои небесные черты.
В глуши, во мраке заточенья
Тянулись тихо дни мои
Без божества, без вдохновенья,
Без слез, без жизни, без любви.
Душе настало пробужденье:
И вот опять явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.
И сердце бьется в упоенье,
И для него воскресли вновь
И божество, и вдохновенье,
И жизнь, и слезы, и любовь."""


with open("pushkin.txt", "w", encoding="utf-8") as file:
    file.write(poem_text)

def count_lines_and_words(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

lines, words = count_lines_and_words("pushkin.txt")
print(f"Количество строк: {lines}")
print(f"Количество слов: {words}")

def count_commas(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        num_commas = content.count(",")
    return num_commas

commas = count_commas("pushkin.txt")
print(f"Количество запятых: {commas}")


def last_line_uppercase(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        last_line = lines[-1].strip()
    return last_line.upper()

last_line_upper = last_line_uppercase("pushkin.txt")
print(f"Последняя строка в верхнем регистре: {last_line_upper}")
