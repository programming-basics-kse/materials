class Book:
    def __init__(self, name, author, content, year):
        self.name = name
        self.author = author
        self.content = content
        self.year = year


def input_book_info():
    name = input("Enter name: ")
    author = input("Enter author: ")
    content = input("Enter content: ")
    year = input("Enter year: ")
    print(f"{name}, {author}, {content}, {year}")


print(input_book_info())