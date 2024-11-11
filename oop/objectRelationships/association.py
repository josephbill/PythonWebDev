class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)


class Book:
    def __init__(self,title):
        self.title = title

#usage
lib1 = Library("Kenya National Library: Upperhill")
book1 = Book("The raising sun")
book2 = Book("The great awakening")
lib1.add_book(book1)
lib1.add_book(book2)
print(lib1.books)

### Library and books objects are associated via the method add_books