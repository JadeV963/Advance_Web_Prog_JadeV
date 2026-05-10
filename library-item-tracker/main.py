from book import Book

book1 = Book("Le petit Prince", " Antoine De Saint_Exupéry", True)
book2 = Book("Corto Maltese", "Hugo Pratt", False)
book3 = Book("Dokkodo", "Miyamoto Musashi", True)

print(book1.title, book1.author, book1.available)
print(book2.title, book2.author, book2.available)
print(book3.title, book3.author, book3.available)

book1.display_info()
book2.display_info()
book3.display_info()

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()
print(Book.library_name)
Book.change_library_name("Gabriel-Roy")
print(Book.library_name)

print(Book.is_valid_title("Inuyasha"))
print(Book.is_valid_title(""))


Book.show_count()

book4 = Book.from_string("Tintin, Hergé, True")
book4.display_info()