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
    book1 = Book("9780984782857", "Cracking the Coding Interview", "Gayle Laakmann McDowell", 2015)
    book2 = Book("9780262033848", "Introduction to Algorithms, Third Edition", "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein", 2009)

    library.add_book(book1)
    library.add_book(book2)

    # View available books
    print("Available Books:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}")

    # Borrow a book
    print("\nBorrowing 'Cracking the Coding Interview'...")
    library.borrow_book("9780984782857")

    # Try viewing available books again
    print("\nAvailable Books after borrowing:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}")

    # Return the borrowed book
    print("\nReturning 'Cracking the Coding Interview'...")
    library.return_book("9780984782857")

    # View available books again
    print("\nAvailable Books after returning:")
    for book in library.view_available_books():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}")

    ``` 
 
  
- Expected Output
    ```plaintext
    Available Books:
    ISBN: 9780984782857, Title: Cracking the Coding Interview, Author: Gayle Laakmann McDowell, Year: 2015  
    ISBN: 9780262033848, Title: Introduction to Algorithms, Third Edition, Author: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, Year: 2009

    Borrowing 'Cracking the Coding Interview'...

    Available Books after borrowing:
    ISBN: 9780262033848, Title: Introduction to Algorithms, Third Edition, Author: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, Year: 2009

    Returning 'Cracking the Coding Interview'...

    Available Books after returning:
    ISBN: 9780984782857, Title: Cracking the Coding Interview, Author: Gayle Laakmann McDowell, Year: 2015  
    ISBN: 9780262033848, Title: Introduction to Algorithms, Third Edition, Author: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, Year: 2009
    ```
   
   