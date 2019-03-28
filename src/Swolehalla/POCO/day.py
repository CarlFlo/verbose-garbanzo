import exercises as ex
class Routine:
    def __init__(self):
        pass

    def showRoutine(self):
        pass


class Day:

    _dayexercises = []

    def __init__(self, name):
        self.name = name

    def addExercise(self, name):
        if name in ex._exercises:
            self._dayexercises.append(name)
        else:
            print("Exercise doesnt exist")

    def printExercises(self):
        print(', '.join(self._dayexercises))
