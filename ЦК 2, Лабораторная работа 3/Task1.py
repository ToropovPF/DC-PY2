import doctest


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация экземпляра класса Book
        :param name: название книги
        :param author: автор книги

        Примеры:
        >>> book = Book('Капитанская дочка', 'А.С Пушкин') # Инициализация экземпляра класса
        """
        self._name = name
        self._author = author

    def __str__(self):
        '''
        Строковый метод класса Book
        :return: возвращает название книги и её автора

        Примеры:
        >>> book = Book('Капитанская дочка', 'А.С Пушкин')
        >>> print(book)
        Книга Капитанская дочка. Автор А.С Пушкин
        '''
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        '''
        Еще один строковый метод, но который возвращает валидную питоновскую строку
        :return: Питоновская строка, которой можно инициализировать объект
        Примеры:
        >>> book = Book('Капитанская дочка', 'А.С Пушкин')
        >>> print(repr(book))
        Book(name='Капитанская дочка', author='А.С Пушкин')
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        '''
        Делает приватный атрибут _name свойством name.
        :return: Возвращает значение свойства name
        Примеры:
        >>> book = Book('Капитанская дочка', 'А.С Пушкин')
        >>> print(book.name)
        Капитанская дочка
        '''
        return self._name

    @property
    def author(self) -> str:
        '''
        Делает приватный атрибут _author свойством author
        :return: Возвращает значение для свойства author
        Примеры:
        >>> book = Book('Капитанская дочка', 'А.С Пушкин')
        >>> print(book.author)
        А.С Пушкин
        '''
        return self._author


class PaperBook(Book):
    """ Дочерний класс. Бумажная книга. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экземпляра класса
        :param name: название книги
        :param author: автор книги
        :param pages: кол-во страниц
        """
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        '''
        Cтроковый метод, но который возвращает валидную питоновскую строку
        :return: Питоновская строка, которой можно инициализировать объект
        Примеры:
        >>> book = PaperBook('Капитанская дочка', 'А.С Пушкин', 300)
        >>> print(repr(book))
        PaperBook(name='Капитанская дочка', author='А.С Пушкин', pages=300)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        '''
        Делает приватный атрибут _pages свойством pages
        :return: Возвращает значение свойства pages
        Примеры
        >>> book = PaperBook('Капитанская дочка', 'А.С Пушкин', 300)
        >>> print(book.pages)
        300
        '''
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        '''
        Сэттер для свойства pages
        :param pages: Новое значение для свойства pages
        :return: Ничего не возвращает. Присваивает новое значение для свойства pages
        Примеры
        >>> book = PaperBook('Капитанская дочка', 'А.С Пушкин', 300)
        >>> book.pages = 'string'
        TypeError: Количество страниц - целое число
        >>> book.pages = -1
        ValueError: Количество страниц не может быть отрицательным
        >>> book.pages = 300
        '''
        if not isinstance(pages, int):
            raise TypeError("Количество страниц - целое число")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self._pages = pages


class AudioBook(Book):
    """ Дочерний класс. Аудиокнига. """

    def __init__(self, name: str, author: str, duration: float):
        '''
        Создание и подготовка к работе объекта AudioBook
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность аудиокниги
        Примеры:
        >>> book = AudioBook('Капитанская дочка', 'А.С. Пушкин', 201.1)
        '''
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        '''
        Cтроковый метод, но который возвращает валидную питоновскую строку
        :return: Питоновская строка, которой можно инициализировать объект
        Примеры:
        >>> book = AudioBook('Капитанская дочка', 'А.С Пушкин', 200.1)
        >>> print(repr(book))
        AudioBook(name='Капитанская дочка', author='А.С Пушкин', duration=200.1)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        '''
        Делает атрибут _duration свойством
        :return: Возвращает значене атрибута duration
        Примеры:
        >>> book = AudioBook('Капитанская дочка', 'А.С Пушкин', 200.1)
        >>> print(book.duration)
        200.1
        '''
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        '''
        Сэттер свойства duration
        :param duration: Новое значение для свойства duration
        :return: Ничего не возвращает. Присваивает новое значение для свойства duration
        Примеры:
        >>> book = AudioBook('Капитанская дочка', 'А.С Пушкин', 200.1)
        >>> book.duration = 'string'
        TypeError: Длительность должна быть типа float
        >>> book.duration = -200
        ValueError: Длительность аудиокниги не может быть отрицательной
        '''
        if not isinstance(duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if duration <= 0:
            raise ValueError("Длительность аудиокниги не может быть отрицательной")
        self._duration = duration


if __name__ == '__main__':
    doctest.testmod()
    # book = PaperBook('Капитанская дочка', 'А.С Пушкин', 300)
    # print(book)
    # print(repr(book))
    # ebook = AudioBook('Капитанская дочка', 'А.С Пушкин', 200.1)
    # print(ebook.duration)
    # print(repr(ebook))
