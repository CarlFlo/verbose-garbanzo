class Animal:

    name = ""
    sound = ""

    def __init__(self):
        pass

    def speak(self):
        print(type(self), self.name, " screams " , self.sound, " and dies")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.sound = "woff"

class Horse(Animal):
    def __init__(self, name):
        self.name = name
        self.sound = "neigh"

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.sound = "meow"

        




