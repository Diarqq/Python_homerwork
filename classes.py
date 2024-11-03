from dataclasses import dataclass, field
from typing import Optional, List, Union

@dataclass
class BookError(Exception):
    """Базовый класс для исключений в книге."""

    def __init__(self, x):
        print(x)

class InvalidPriceError(BookError):
    """Ошибка, возникающая при неверной цене книги."""
    pass

class InvalidPagesError(BookError):
    """Ошибка, возникающая при неверном количестве страниц книги."""
    pass

class InvalidYearError(BookError):
    """Ошибка, возникающая при неверном годе публикации книги."""
    pass

@dataclass
class Book:
    pages: int
    year: int
    author: str
    price: int
    book_id: Optional[int] = field(default=None)

    def __post_init__(self):
        if self.price < 0:
            raise InvalidPriceError("Цена книги не может быть отрицательной.")
        if self.pages <= 0:
            raise InvalidPagesError("Количество страниц должно быть положительным.")
        if self.year < 0:
            raise InvalidYearError("Год публикации не может быть отрицательным.")
        

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.next_id: int = 1

    def add_book(self, book: Book):
        if book.book_id is None:
            book.book_id = self.next_id
            self.next_id += 1
        self.books.append(book)

    def get_book_info(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_books_by_author(self, author: Union[str, List[str]]) -> List[Book]:
        if isinstance(author, str):
            return [book for book in self.books if book.author == author]
        elif isinstance(author, list):
            return [book for book in self.books if book.author in author]
        else:
            raise ValueError("Аргумент 'author' должен быть строкой или списком строк.")



