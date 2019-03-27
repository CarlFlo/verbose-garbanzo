from os import system


class Person:

    def __init__(self, name="undefined", age=-1):
        self.name = name
        self.age = age

    def sayHello(self):
        print(str.format("{} säger hej!", self.name))


class PersonManager:

    people = []

    def addPerson(self, name, age):
        personTmp = Person(name, age)
        self.people.append(personTmp)

    def getPerson(self, index):
        if (index > len(self.people) or index < 0):
            return

        return self.people[index]

    def yieldPeople(self):
        for person in self.people:
            yield person

    def getTotal(self):
        return len(self.people)

    def printTotal(self):
        print(len(self.people), "people")

    def sayHello(self):
        print("Hej från personmanager")


manager = PersonManager()
manager.addPerson("Person 1", 50)
manager.addPerson("Person 2", 25)
manager.addPerson("Person 3", 32)

system("cls")

for person in manager.yieldPeople():
    print(person.sayHello())
