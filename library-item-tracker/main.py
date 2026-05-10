from book import Book

book1 = Book("Le petit Prince", " Antoine De Saint_Exupéry", True)
book2 = Book("Corto Maltese", "Hugo Pratt", False)
book3 = Book("Dokkodo", "Miyamoto Musashi", True)

print(book1.title, book1.author, book1.available)
print(book2.title, book2.author, book2.available)
print(book3.title, book3.author, book3.available)

print(Book.library_name)
Book.change_library_name("Gabriel-Roy")
print(Book.library_name)

print(Book.is_valid_title("Inuyasha"))
print(Book.is_valid_title(""))