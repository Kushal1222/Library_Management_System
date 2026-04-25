from utils import issue_books, books

# Return an issued book back to available
def return_book():
    book_name = input("Enter book name to return: ").upper()
    if book_name in issue_books:
        books[book_name]["available"] = True
        del issue_books[book_name]
        print(f"Book '{book_name}' returned successfully!")
    else:
        print("This book was not issued!")