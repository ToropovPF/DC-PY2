BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
                Создание и подготовка к работе объекта "Книга"
                :param id_: идентификатор книги
                :param name: название книги
                :param pages: количество страниц книги
                Пример:
                #>>> book = Book(id_=25, name="abc", pages=20)  # инициализация экземпляра класса
           """

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    """
            Создание и подготовка к работе объекта "Библиотека"
            :param books: список книг
            Пример:
            #>>> library = Library(Book(id_=25, "id": 2,"name": "test_name_5", "pages": 100)  # инициализация экземпляра класса
        """

    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса"""
        for i, books in enumerate(self.books):
            if books.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
