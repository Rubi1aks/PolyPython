class Library:
    def __init__(self, books=None):
        """
        Инициализация экземпляра класса Library.

        :param books: Список книг в библиотеке (по умолчанию пустой список).
        """
        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типом list")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для новой книги в библиотеке.

        :return: Следующий идентификатор книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с запрашиваемым идентификатором нет.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра класса Book.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги в формате:
        Книга "название_книги"

        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку для создания нового экземпляра Book.
         """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"

# Используем ранее определённый класс Book
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

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
