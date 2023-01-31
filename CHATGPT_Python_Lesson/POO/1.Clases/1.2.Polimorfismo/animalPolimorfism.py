class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()

print(animal_sound(dog)) # Output: "Woof!"
print(animal_sound(cat)) # Output: "Meow!"
