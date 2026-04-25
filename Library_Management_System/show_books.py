from utils import books
# Show all available books in a formatted table
def show():
    available = {k: v for k, v in books.items() if v["available"] == True}
    if len(available) == 0:
        print("No books available!")
    else:
        print("\n" + "="*55)
        print(f"{'SR':<5} {'BOOK NAME':<25} {'AUTHOR':<20} {'GENRE'}")
        print("="*55)
        for i, (name, details) in enumerate(available.items(), 1):
            print(f"{i:<5} {name:<25} {details['author']:<20} {details['genre']}")
        print("="*55)