class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        if self.available:
            self.available = "Book Available"
        else:
            self.available = "Book Not Available" 

        print(f"Title: {self.title}, Author: {self.author}, available: {self.available}")