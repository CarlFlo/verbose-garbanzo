from typing import Dict

import muscle as mu


class muscles:

    _muscles: Dict[str, mu.muscle] = {}

    def addMuscle(self, muscle):
        self._muscles[muscle.getName()] = muscle

    def addMuscles(self, *muscles):

        for e in muscles:
            self._muscles[e.getName()] = e

    def getNumOfMuscles(self):
        return len(self._muscles)

    def yieldMuscles(self):
        for val in self._muscles.values():
            yield val

    def getMuscle(self, name):
        return self._muscles[name]
