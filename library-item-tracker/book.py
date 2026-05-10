class Book:
    library_name = "library of Paris"
    def __init__(self, title, author, available):
        
        self.title = title
        self.author = author
        self.available = available

@classmethod
def change_library_name(cls, new_name):
    cls.library_name = new_name

@staticmethod
def is_valid_title(title):
    return len(title) > 0