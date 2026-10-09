# Библиотека
class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
    def get_info(self):
        return f'{self.title} - {self.author}'
class Library:
    def __init__(self):
        self.book_list=[]
    def add_book(self,book):
        self.book_list.append(book)
    # def get_books(self):
    #     self.result=[]
    #     for i in self.book_list:
    #         self.result.append(i.title)
    #     return print((self.result))
    def find_by_author(self,author):
        self.result=[]
        self.author=author
        for i in self.book_list:
            if i.author.lower()==self.author.lower():
                self.result.append(i.title)
        return self.result

book1=Book('Капитанская дочка', 'Александр Пушкин')
book2=Book('Колотушкин', 'Александр Пушкин')
print(book1.get_info())
print(book2.get_info())

library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(Book('Дубровский', 'александр пушкин'))
print(library.book_list)
print(library.find_by_author('Александр ПУшкин'))