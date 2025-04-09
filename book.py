class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
    
    def read(self):
        print(f"You're reading \"{self.title}\" by {self.author}.")

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"

# Inheritance Example
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_format):
        super().__init__(title, author, genre, pages)
        self.file_format = file_format

    def download(self):
        print(f"Downloading \"{self.title}\" in {self.file_format} format.")

# Creating objects
book1 = Book("1984", "George Orwell", "Dystopian", 328)
ebook1 = EBook("Sapiens", "Yuval Noah Harari", "History", 512, "PDF")

# Using methods
print(book1.get_details())
book1.read()
ebook1.download()
