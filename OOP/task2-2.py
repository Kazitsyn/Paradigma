class Book:
    def __init__(self, name_book, author):
        self.name_book = name_book
        self.author = author

    def toString(self):
        print(self.author, self.name_book)


class Library:
    def __init__(self):
        self.library = []

    def add_book(self, book):
        self.library.append(book)
        print("Книга добавлена в библиотеку.")

    def display_books(self):
        if not self.library:
            print("Библиотека пуста.")
        else:
            print("Список книг в библиотеке:")
            for book in self.library:
                book.toString()


library = Library()
book1 = Book("Star Wars 1", "J.Lucas")
book2 = Book("Star Wars 2", "J.Lucas")

book1.toString()

while True:
    print("\n1. Добавить книгу")
    print("2. Показать список книг")
    print("3. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        author = input("Введите автора: ")
        name_book = input("Введите название книги: ")
        book = Book(author, name_book)
        library.add_book(book)


    elif choice == "2":
        library.display_books()
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")