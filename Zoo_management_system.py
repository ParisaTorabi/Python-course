class Animal:
    def __init__(self, name, species, age, sound, zoo_name):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name

    def __str__(self):
        return f"Animal name is {self.name}, its species is {self.species}, it is {self.age} years old,and it makes a {self.sound} sound!"

    def make_sound(self):
        print(self.sound)

    def info(self):
        print(
            f"name: {self.name},\nspecies: {self.species},\nage:{self.age}, \nsound: {self.sound},\nzoo name: {self.zoo_name}"
        )


class Bird(Animal):
    def __init__(self, name, species, age, sound, zoo_name, wing_span):
        super().__init__(name, species, age, sound, zoo_name)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"Bird sound: {self.sound}")


Lion = Animal(
    name="Mufasa", species="Panthera leo", age=5, sound="roar", zoo_name="San Diego Zoo"
)
print(Lion)

Lion.make_sound()

Lion.info()

Raven = Bird("Captain Crwo", "Crow", 2, "coo", "Oslo zoo", 100)
Raven.make_sound()
