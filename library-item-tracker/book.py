class Book:
    library_name = "library of Paris"
    count = 0
    def __init__(self, title, author, available):
        Book.count += 1
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print(f"BRANCH VERSION: {self.title} by {self.author}")
        print(f"----------------------------------------")
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed!")
            print(f"----------------------------------------")
        else:
            print(f"{self.title} is not available")
            print(f"----------------------------------------")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned!")
        print(f"----------------------------------------")
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        return len(title) > 0
    
    @classmethod
    def show_count(cls):
        print(f"Total books: {cls.count}")

    @classmethod
    def from_string(cls, data):
        pieces = data.split(",")
        return cls(pieces[0], pieces[1], pieces[2] == "True")
