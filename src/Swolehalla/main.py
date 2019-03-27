from os import system
import swole

system("cls")

biceps = swole.muscle("Biceps", "desc")
Triceps = swole.muscle("Triceps", "desc")
DeltoidAnterior = swole.muscle("Deltoid Anterior", "desc")
Pectoralis = swole.muscle("Pectoralis", "desc")

_muscles = swole.muscles()
_muscles.addMuscle(biceps)

bench = swole.exercise("Flat Barbell Bench Press", {Triceps, DeltoidAnterior, Pectoralis})

myExercises = swole.exercises()
myExercises.addExercise(bench)

myExercises.searchTargetMuscle("Triceps")

"""
for e in bench.getTargetMuscles():
    print(e.getName(), e.getDescription())
"""
