from api_Library import Book, Library


library = Library()
book_1 = Book(title="Капитанская дочка",
              author="Пушкин",
              year=1836,
              genre="роман")

book_2 = Book(title="Герой нашего времени",
              author="Лермонтов",
              year=1855,
              genre="роман")

library.add_book(book_1)
library.add_book(book_2)

books = library.get_books()
for id_, book in books.items():
    print(book.get_info())