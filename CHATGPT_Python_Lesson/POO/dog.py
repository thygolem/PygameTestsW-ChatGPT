class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Canis lupus familiaris")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def make_sound(self):
        print("Woof!")
