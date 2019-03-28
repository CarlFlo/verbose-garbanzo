from enum import Enum
from typing import Dict

import muscle as mu


class ExerciseDifficulty(Enum):
    EASY = 'beginner'
    MEDIUM = 'intermediate'
    HARD = 'expert'

    @classmethod
    def hasValue(cls, value):
        return any(value == item.value for item in cls)


class exercise:

    _muscles: Dict[str, mu.muscle] = {}

    def __init__(self, name, difficulty, muscleArr):
        if not ExerciseDifficulty.hasValue(difficulty):
            raise ValueError('difficulty not valid', difficulty)

        self.name = name
        self._muscles = {}
        for e in muscleArr:
            self._muscles[e.getName()] = e

    def getName(self):
        return self.name

    def getTargetMuscles(self):
        return self._muscles

    def getTargetMuscle(self, name):

        try:
            data = self._muscles[name]
            return data
        except Exception:
            pass
        return None
