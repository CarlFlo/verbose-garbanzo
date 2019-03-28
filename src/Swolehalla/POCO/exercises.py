from typing import Dict

import exercise as ex


class exercises:

    _exercises: Dict[str, ex.exercise] = {}

    def addExercise(self, exercise):
        self._exercises[exercise.getName()] = exercise

    def addExercises(self, *exercise):
        for e in exercise:
            self._exercises[e.getName()] = e

    def searchTargetMuscleInExercises(self, name):

        result = {}

        for exercise in self._exercises.values():

            if(exercise.getTargetMuscle(name) is None):
                continue

            result[exercise.getName()] = exercise
