class Book(object) :
    def __init__(self, title, isbn) :
        self._title = title
        self. _isbn = isbn
    def __str__(self) :
        return " Title : " + self._title + "\t"+ " isbn : " + self._isbn
    
book = Book("The Python Turtorial", "0123456")
print(book)