# Library Management System

## **Overview**
A Python-based library management system allowing users to add books, borrow books, return books, and view available books.

## **Setup**

1. Clone the repository:
   ```bash 
   git clone https://github.com/neel-jotaniya/library-management-system.git
   cd library_management
   ``` 

2. Install dependencies:
   ```bash 
    pip install -r requirements.txt
   ``` 

2. Run the test suite to ensure everything works correctly:
    ```bash 
   pytest
   ``` 


## **Example Usage**

Import the Library and Book classes in your Python project to use the library system:

- Code Example

    ```python
    from src.library import Book, Library
    # Initialize the library
    library = Library()
    
    # Add books to the library
    book1 = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald",     1925)
    book2 = Book("987654321", "To Kill a Mockingbird", "Harper Lee", 1960)
    
    library.add_book(book1)
    library.add_book(book2)
    
    # View available books
    print("Available Books:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author:     {book.author}, Year: {book.year}")
    
    # Borrow a book
    print("\nBorrowing 'The Great Gatsby'...")
    library.borrow_book("123456789")
    
    # Try viewing available books again
    print("\nAvailable Books after borrowing:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author:     {book.author}, Year: {book.year}")
    
    # Return the borrowed book
    print("\nReturning 'The Great Gatsby'...")
    library.return_book("123456789")
    
    # View available books again
    print("\nAvailable Books after returning:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author:     {book.author}, Year: {book.year}")
   ``` 
 
  
- Expected Output
    ```plaintext
    Available Books:
    ISBN: 123456789, Title: The Great Gatsby, Author: F. Scott Fitzgerald,     Year: 1925
    ISBN: 987654321, Title: To Kill a Mockingbird, Author: Harper Lee, Year:     1960
    
    Borrowing 'The Great Gatsby'...
    
    Available Books after borrowing:
    ISBN: 987654321, Title: To Kill a Mockingbird, Author: Harper Lee, Year:     1960
    
    Returning 'The Great Gatsby'...
    
    Available Books after returning:
    ISBN: 123456789, Title: The Great Gatsby, Author: F. Scott Fitzgerald,     Year: 1925
    ISBN: 987654321, Title: To Kill a Mockingbird, Author: Harper Lee, Year:     1960

    ```
   
   