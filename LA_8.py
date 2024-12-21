class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Python Programming", "John Doe")
print(f"Author: {book.author}")

del book.author

print(book.author)  
