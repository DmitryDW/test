class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_factory(animal_type, name):
    if animal_type == "dog":
        return Dog(name)
    elif animal_type == "cat":
        return Cat(name)

dog = animal_factory("dog", "Fido")
cat = animal_factory("cat", "Fluffy")

print(dog.speak())
print(cat.speak())
