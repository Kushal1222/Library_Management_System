from utils import books, issue_books

# Issue a book to a student if it is available
def issue():
    book_name = input("Enter book name to issue: ").upper()
    if book_name in books and books[book_name]["available"] == True:
        books[book_name]["available"] = False
        issue_books[book_name] = books[book_name]
        print(f"Book '{book_name}' issued successfully!")
    else:
        print("Book not available or already issued!")