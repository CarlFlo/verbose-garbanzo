class Routine:
    def __init__(self):
        pass

    def showRoutine(self):
        pass


class muscle:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def getName(self):
        return self.name

    def getDescription(self):
        return self.desc


class muscles:

    _muscles = {}

    def addMuscle(self, muscle):
        self._muscles[muscle.getName] = muscle

    def getMuscle(self, name):
        return self._muscles[name]


class exercise:

    def __init__(self, name, muscle):
        self.name = name
        self.name = muscle  # hämta från muscles klassen


class exercises:

    _exercises = {}

    def addExercise(self, exercise):
        pass
