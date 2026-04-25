from utils import books

# Ask book name, author and genre and add to books dictionary
def add():
    book_name = input("Enter book name: ").upper()
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    books[book_name] = {"author": author, "genre": genre, "available": True}
    print(f"Book '{book_name}' added successfully!")
    