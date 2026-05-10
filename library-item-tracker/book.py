class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been Borrowed!")
        else:
            print(f"{self.title} is not available.")
    
    def returned_book(self):
        self.available = True
        print(f"{self.title} has been returned!")

    def display_info(self):
        print(f"Title: {self.title}, Author:{self.author}, Available:{self.available}")