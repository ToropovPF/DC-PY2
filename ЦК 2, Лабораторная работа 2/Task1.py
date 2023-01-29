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
                  #>>> book = Book(id_=10, name="test_name_3", pages=500)  # инициализация экземпляра класса
             """
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_  # идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
