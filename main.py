import classes
library = classes.Library()

book1 = classes.Book(pages=300, year=2020, author="Автор 1", price=500.0)
library.add_book(book1)

book2 = classes.Book(pages=250, year=2019, author="Автор 2", price=300.0)
library.add_book(book2)

book3 = classes.Book(pages=150, year=2021, author="Автор 1", price=700.0)
library.add_book(book3)

    # Получить информацию о книге по ID
book_info = library.get_book_info(1)
print(book_info)

    # Поиск книг по автору
books_by_author1 = library.search_books_by_author("Автор 1")
print(books_by_author1)

    # Поиск книг сразу по нескольким авторам
books_by_authors = library.search_books_by_author(["Автор 1", "Автор 2"])
print(books_by_authors)
