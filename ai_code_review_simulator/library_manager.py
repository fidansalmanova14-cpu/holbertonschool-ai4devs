import datetime

class Book:
    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.due_date = None

    def __repr__(self):
        return f"Book({self.title} by {self.author})"

class Library:
    def __init__(self):
        self.books = {}
        self.audit_log = []

    def add_book(self, title, author, isbn):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, isbn)
        self.books[book_id] = new_book
        self.audit_log.append(f"Added: {title}")
        return book_id

    def search_books(self, query):
        """Search books by title or author."""
        results = []
        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results

    def checkout_book(self, book_id, days=14):
        if book_id not in self.books:
            return "Book not found."
        
        book = self.books[book_id]
        if not book.is_available:
            return "Book is already checked out."
        
        book.is_available = False
        book.due_date = datetime.date.today() + datetime.timedelta(days=days)
        self.audit_log.append(f"Checked out: {book.title} until {book.due_date}")
        return f"Success. Due date: {book.due_date}"

    def return_book(self, book_id):
        if book_id not in self.books:
            return "Book not found."
        
        book = self.books[book_id]
        book.is_available = True
        book.due_date = None
        self.audit_log.append(f"Returned: {book.title}")
        return "Book returned successfully."

    def get_overdue_books(self):
        today = datetime.date.today()
        overdue = []
        for book in self.books.values():
            if not book.is_available and book.due_date < today:
                overdue.append(book)
        return overdue

# Example usage/Simple simulation
if __name__ == "__main__":
    lib = Library()
    lib.add_book("1984", "George Orwell", "12345")
    lib.add_book("Clean Code", "Robert Martin", "67890")
    print(lib.search_books("Clean"))
    print(lib.checkout_book(1))
