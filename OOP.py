# %%
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


# %% Inheritance


class Educational(Book):
    def __init__(self, name, pages, major, seniority):
        super().__init__(name, pages)
        self.major = major
        self.seniority = seniority


eb1 = Educational("Biology tests", 234, "natural sciences", "Sophomore")

print(eb1.name)
eb1.open_a_random_page()
print(eb1.seniority)

# %% overriding...


class fiction(Book):
    genre = "Fiction"

    def open_a_random_page(self):
        print(f"Opened the last page {self.pages}, because fiction works like that!")


fb = fiction("Harry Potter and the Goblet of Fire", 636)
fb.open_a_random_page()
print(fb.genre)

# %% On polymorphism


class Runner:
    def __init__(self, name: str):
        self.name = name

    def act(self):
        print(f"{self.name} is running.")


class Cyclist:
    def __init__(self, name: str):
        self.name = name

    def act(self):
        print(f"{self.name} is biking.")


Parisa = Cyclist("Parisa")
Erfan = Runner("Erfan")

for person in [Parisa, Erfan]:
    person.act()  # Interesting!!

# %% abstract methods
