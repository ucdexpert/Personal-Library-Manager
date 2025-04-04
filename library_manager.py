import csv

def add_book(library):
    print("\nAdd a book")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        year = input("Enter the publication year: ").strip()
        try:
            year = int(year)
            break
        except ValueError:
            print("Invalid year. Please enter a valid integer.")
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    while read_status not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_status == 'yes'
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    print("\nRemove a book")
    title = input("Enter the title of the book to remove: ").strip()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'] != title]
    if len(library) < initial_length:
        print("Book removed successfully!")
    else:
        print("No book found with that title.")

def search_books(library):
    print("\nSearch for a book")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
    search_term = input("Enter the search term: ").strip()
    results = []
    if choice == '1':
        results = [book for book in library if book['title'] == search_term]
    else:
        results = [book for book in library if book['author'] == search_term]
    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books found.")

def display_all(library):
    print("\nDisplay all books")
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_stats(library):
    print("\nDisplay statistics")
    total = len(library)
    print(f"Total books: {total}")
    if total == 0:
        print("Percentage read: 0.0%")
        return
    read_count = sum(1 for book in library if book['read'])
    percentage = (read_count / total) * 100
    print(f"Percentage read: {percentage:.1f}%")

def load_library(filename):
    library = []
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != 5:
                    continue
                title, author, year, genre, read = row
                try:
                    year = int(year)
                    read = read == 'True'
                except ValueError:
                    continue
                library.append({
                    'title': title,
                    'author': author,
                    'year': year,
                    'genre': genre,
                    'read': read
                })
    except FileNotFoundError:
        pass
    return library

def save_library(library, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for book in library:
            writer.writerow([book['title'], book['author'], str(book['year']), book['genre'], str(book['read'])])

def main():
    filename = "library.txt"
    library = load_library(filename)
    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_all(library)
        elif choice == '5':
            display_stats(library)
        elif choice == '6':
            save_library(library, filename)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()