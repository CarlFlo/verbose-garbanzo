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

####


class muscles:

    _muscles = {}

    def addMuscle(self, muscle):
        self._muscles[muscle.getName()] = muscle

    def getMuscle(self, name):
        return self._muscles[name]


class exercise:

    def __init__(self, name, muscles):
        self.name = name
        self.muscles = {}
        for e in muscles:
            self.muscles[e.getName] = e

    def getName(self):
        return self.name

    def getTargetMuscles(self):
        return self.muscles

    def getTargetMuscle(self, name):
        return self.muscles[name]


####
class exercises:

    _exercises = {}

    def addExercise(self, exercise):
        self._exercises[exercise.getName()] = exercise

    def searchTargetMuscle(self, name):
        for key in self._exercises:
            e = self._exercises[key]

            data = e.getTargetMuscle(name)

            if(data is not None):
                print(e.getName())
