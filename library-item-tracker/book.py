class Book:
    library_name = "library of Paris"
    def __init__(self, title, author, available):
        
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        def display_info(self):
            print(f"MAIN VERSION: {self.title} by {self.author}")
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
