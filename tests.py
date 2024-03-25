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

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Записки юного врача')
        assert len(collector.get_books_genre()) == 1

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.add_book_in_favorites('Трое в лодке, не считая собаки')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')

        collector.add_new_book('За двумя зайцами')
        collector.set_book_genre('За двумя зайцами', 'Комедии')

        books_genre = collector.get_books_genre()
        assert books_genre == {'Пикник на обочине': 'Фантастика',
                               'За двумя зайцами': 'Комедии'}

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        collector.add_new_book('Кот Саймона')
        collector.add_book_in_favorites('Кот Саймона')

        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books == ['Гарри Поттер и философский камень', 'Кот Саймона']

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Звёздный десант')
        collector.set_book_genre('Звёздный десант', 'Фантастика')
        book_genre = collector.get_book_genre('Звёздный десант')

        assert book_genre == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')

        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Драма')

        assert collector.get_books_with_specific_genre('Детективы') == ['Преступление и наказание']

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Три кота')
        collector.set_book_genre('Три кота', 'Мультфильмы')

        collector.add_new_book('Простоквашино')
        collector.set_book_genre('Простоквашино', 'Комедии')

        assert collector.get_books_for_children() == ['Три кота', 'Простоквашино']

    def test_get_books_for_children_add_book_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()

    def test_add_new_book_add_book_with_long_name(self):
        collector = BooksCollector()

        collector.add_new_book('Собачье сердце. Записки юного врача. Роковые яйца. Дьяволиада. Записки на манжетах ('
                               'сборник)')

        assert len(collector.get_books_genre()) == 0