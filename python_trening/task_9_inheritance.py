class Mammal:
    className = 'Млекапитающие'

class Dog(Mammal):
    special = 'Canis lupus'

dog = Dog()
print(dog.className)