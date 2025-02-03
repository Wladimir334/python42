

def main():
    words = []
    while True:
        word = input("Введите слово: ")
        if word == "":
            break
        if word not in words:
            words.append(word)

    print("Введенные слова:")
    for word in words:
        print(word)

main()
