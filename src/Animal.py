class Animal:

    name = ""

    def __init__(self):
        pass

    def speak(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name):
        self.name = name

