from typing import Dict, List

class Book:
    def __init__(self, isbn: str, title: str, author: str, year: int) -> None:
        """
        Initialize a new Book object.

        :param isbn: Unique identifier for the book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Publication year of the book.
        """
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.is_borrowed: bool = False  # Flag indicating if the book is currently borrowed.

    def __str__(self) -> str:
        """
        String representation of the book.
        :return: A string describing the book.
        """
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self) -> None:
        """
        Initialize a new Library object.
        """
        self.books: Dict[str, Book] = {}  # Dictionary to store books, keyed by their ISBN.

    def add_book(self, book: Book) -> None:
        """
        Add a new book to the library.

        :param book: The Book object to add.
        :raises ValueError: If a book with the same ISBN already exists.
        """
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def borrow_book(self, isbn: str) -> None:
        """
        Borrow a book from the library.

        :param isbn: ISBN of the book to borrow.
        :raises ValueError: If the book is not found or is already borrowed.
        """
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise ValueError("Book is already borrowed.")
        book.is_borrowed = True

    def return_book(self, isbn: str) -> None:
        """
        Return a borrowed book to the library.

        :param isbn: ISBN of the book to return.
        :raises ValueError: If the book is not found or is not borrowed.
        """
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if not book.is_borrowed:
            raise ValueError("Book is not borrowed.")
        book.is_borrowed = False

    def view_available_books(self) -> List[Book]:
        """
        View all available (not borrowed) books in the library.

        :return: A list of available Book objects.
        """
        return [book for book in self.books.values() if not book.is_borrowed]
