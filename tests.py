import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # проверка связи

    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем что добавилась только одна книга
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1

        # проверяем добавление рейтинга больше 10

    def test_set_book_rating_more_that_10(self):
        collector = BooksCollector()

        # добавляем книгу
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.set_book_rating(book, 11)

        assert collector.books_rating.get(book) != 11

    def test_set_book_rating_less_that_1(self):
        collector = BooksCollector()

        # добавляем книгу
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.set_book_rating(book, 0)

        assert collector.books_rating.get(book) != 0

    @pytest.mark.parametrize(
        'book, rating',
        [
            ['Гордость и предубеждение и зомби', 5],
            ['Что делать, если ваш код хочет вас убить', 7],
            ['Что делать если ваш зомби - кот', 7]
        ]
    )
    def test_get_books_with_specific_rating_with_7(self, book, rating):
        collector = BooksCollector()

        # добавляем две книги и устанавливаем им рейтинг
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)
        collector.get_books_with_specific_rating(7)

        # проверяем, что длина словаря books_with_specific_rating равна 2
        assert len(collector.books_with_specific_rating) == 2

    # метод set_book_rating не записал рейтинг больше 10
    @pytest.mark.parametrize('rating', [11])
    def test_set_book_rating_less_that_1_and_more_that_10(self, rating):
        collector = BooksCollector()

        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)

        assert collector.get_book_rating(book) != 11

    # добавлем книгу в избранное, которой нет в books_rating
    def test_add_book_in_favorites_which_is_not_in_books_rating(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гордость и предубеждение и не зомби')

        assert len(collector.favorites()) == 0

    # добавлем две книги в избранное
    def test_add_book_in_favorites_two_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites()) == 2

    # проверяем что книга не добавилась два раза в избранное
    def test_add_book_in_favorites_one_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites()) == 1

    # проверяем удаление одной книги из избранного 123
    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites()) == 1