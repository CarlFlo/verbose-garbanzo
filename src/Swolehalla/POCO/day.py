from .exercises import exercises as ex


class Day:

    _dayexercises = []

    def __init__(self, name):
        self.name = name

    def addExercise(self, name):
        if name in ex._exercises:
            self._dayexercises.append(name)
        else:
            print("Exercise doesnt exist:", name)

    def printExercises(self):
        print(', '.join(self._dayexercises))
