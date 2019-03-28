from os import system
from typing import Dict

from POCO import day, exercise, exercises, muscle, muscles


class Program:

    def run(self):
        biceps = muscle.muscle("Biceps", "desc")
        triceps = muscle.muscle("Triceps", "desc")
        deltoidAnterior = muscle.muscle("Deltoid Anterior", "desc")
        pectoralis = muscle.muscle("Pectoralis", "desc")

        _muscles = muscles.muscles()
        _muscles.addMuscles(biceps, triceps, deltoidAnterior, pectoralis)

        for e in _muscles.yieldMuscles():
            print(e.getName())

        bench = exercise.exercise("Flat Barbell Bench Press", "intermediate", {
            triceps, deltoidAnterior, pectoralis})
        pushups = exercise.exercise("Pushups", "beginner", {
            triceps, deltoidAnterior, pectoralis})

        myExercises = exercises.exercises()
        myExercises.addExercises(bench, pushups)

        myExercises.searchTargetMuscleInExercises("Triceps")

        day1 = day.Day("push")
        day1.addExercise("Flat Barbell Bench Press")
        day1.addExercise("Squat Barbell Bench Curl")
        day1.addExercise("Pushups")
        while(True):
            
            print("--------------------------------------")
            print("welcome to davcar's ultimate swole app")
            print("Create day")
            ans = input()
            day = day.Day("ans")
            print("Show your exercises(y/n)")
            ans = input()
            if ans == "y":
                day1.printExercises()
            else:
                print("Ok then, keep your secrets")



system("cls")
program = Program()
try:
    program.run()
except Exception as e:
    print("In my country there is problem\n", e)
finally:
    print("is it working?")
