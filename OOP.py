import random


class Book:
    genre = "Sci-Fi"

    def __init__(self, name, pages):
        self.pages = pages
        self.name = name

    def open_a_random_page(self):
        print(f"Opened page {random.randint(1, self.pages)} of the book {self.name}.")


my_book = Book(name="Animal farm", pages=300)
# print(my_book.pages)

my_book.open_a_random_page()
print(my_book.genre)
Book.genre = "Romance"
print(my_book.genre)


# %%


class Circle:
    pi = 3.1415926

    def __init__(self, r: float):
        self.r = r

    def compute_area(self):
        return Circle.pi * (self.r**2)


C1 = Circle(4)
print(C1.compute_area())
