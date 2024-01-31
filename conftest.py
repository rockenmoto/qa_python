import pytest

from main import BooksCollector


# Метод для инициализации класса
@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


# Метод для добавления 1-й книги "Гордость и предубеждение и зомби"
@pytest.fixture(scope='function')
def add_book(collector):
    book_name = 'Гордость и предубеждение и зомби'
    collector.add_new_book(book_name)
    return book_name


# Метод для получения жанра "Ужасы"
@pytest.fixture(scope='function')
def horror_genre(collector, add_book):
    collector.set_book_genre(add_book, 'Ужасы')
    return collector.get_book_genre(add_book)
