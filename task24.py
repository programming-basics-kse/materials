class Book:
    def __init__(self, name, author, content, year): #використала тому що треба ініціювати змінні
        self.name = name
        self.author = author
        self.content = content
        self.year = year

    def def_to_dict(self): #створила словник що б зв'язати змінні з ключами
        dictionary = {
            "name": self.name,
            "author": self.author,
            "content": self.content,
            "year": self.year
        }
        return dictionary


book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
print(book.def_to_dict())
