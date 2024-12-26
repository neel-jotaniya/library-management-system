import pytest
from src.library import Book, Library

@pytest.fixture
def library():
    return Library()

@pytest.fixture
def sample_book():
    return Book("123456789", "Sarcasm 101: A Masterclass", "Chandler Bing", 2024)

def test_add_book(library, sample_book):
    library.add_book(sample_book)
    assert sample_book.isbn in library.books

def test_add_duplicate_book(library, sample_book):
    library.add_book(sample_book)
    with pytest.raises(ValueError, match="Book with this ISBN already exists."):
        library.add_book(sample_book)

def test_borrow_book(library, sample_book):
    library.add_book(sample_book)
    library.borrow_book(sample_book.isbn)
    assert sample_book.is_borrowed

def test_borrow_nonexistent_book(library):
    with pytest.raises(ValueError, match="Book not found."):
        library.borrow_book("000000000")

def test_borrow_already_borrowed_book(library, sample_book):
    library.add_book(sample_book)
    library.borrow_book(sample_book.isbn)
    with pytest.raises(ValueError, match="Book is already borrowed."):
        library.borrow_book(sample_book.isbn)

def test_return_book(library, sample_book):
    library.add_book(sample_book)
    library.borrow_book(sample_book.isbn)
    library.return_book(sample_book.isbn)
    assert not sample_book.is_borrowed

def test_return_nonexistent_book(library):
    with pytest.raises(ValueError, match="Book not found."):
        library.return_book("000000000")

def test_return_not_borrowed_book(library, sample_book):
    library.add_book(sample_book)
    with pytest.raises(ValueError, match="Book is not borrowed."):
        library.return_book(sample_book.isbn)

def test_view_available_books(library, sample_book):
    library.add_book(sample_book)
    available_books = library.view_available_books()
    assert len(available_books) == 1
    assert available_books[0] == sample_book
