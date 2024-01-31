import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # Проверка метода add_new_book
    def test_add_new_book_add_two_books_added(self, collector, add_book):
        # добавление второй книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_name_book_with_existing_genre_not_added(self, collector, add_book, horror_genre):
        collector.set_book_genre(add_book, horror_genre)
        collector.add_new_book(add_book)
        assert len(collector.get_books_genre()) == 1

    # Проверка метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_specific_genre(self, collector, add_book):
        collector.set_book_genre(add_book, collector.genre[1])
        assert add_book in collector.get_books_with_specific_genre(collector.genre[1])

    @pytest.mark.parametrize('genre', ['Ужасы', 'Индийская комедия'])
    def test_get_books_with_specific_genre_unspecific_genre(self, collector, add_book, genre):
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    # Проверка метода get_books_for_children
    @pytest.mark.parametrize('kid_book, kid_genre', [['Том Соер', 'Комедии'], ['Простоквашино', 'Мультфильмы']])
    def test_get_books_for_children_children_books_with_children_genres(self, collector, kid_book, kid_genre):
        collector.add_new_book(kid_book)
        collector.set_book_genre(kid_book, kid_genre)
        assert kid_book in collector.get_books_for_children()

    @pytest.mark.parametrize('not_kid_book, not_kid_genre', [['ОНО', 'Ужасы'], ['Борат', 'Сатира']])
    def test_get_books_for_children_not_children_books_with_not_children_genres(self, collector, not_kid_book,
                                                                                not_kid_genre):
        collector.add_new_book(not_kid_book)
        collector.set_book_genre(not_kid_book, not_kid_genre)
        assert not_kid_book not in collector.get_books_for_children()

    # Проверка метода add_book_in_favorites
    def test_add_book_in_favorites_specific_book_name_added(self, collector, add_book):
        collector.add_book_in_favorites(add_book)
        assert add_book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_specific_book_name_not_added_twice(self, collector, add_book):
        collector.add_book_in_favorites(add_book)
        collector.add_book_in_favorites(add_book)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_unspecific_name_not_added(self, collector, add_book):
        collector.add_book_in_favorites('add_book')
        assert len(collector.get_list_of_favorites_books()) == 0

    # Проверка метода delete_book_from_favorites
    def test_delete_book_from_favorites_specific_book_name_deleted(self, collector, add_book):
        collector.add_book_in_favorites(add_book)
        collector.delete_book_from_favorites(add_book)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_test_delete_book_from_favorites(self, collector):
        collector.delete_book_from_favorites('add_book')
        assert len(collector.get_list_of_favorites_books()) == 0
