class Animal:

    name = ""
    sound = ""

    def __init__(self):
        pass

    def speak(self):
        print(self.name)
        print(self.sound)

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        sound = "woff"
        
class Cat(Animal):
    def _init_(self,name):
        self.name = name
        sound = "meow"
        




