import swole

biceps = swole.muscle("Biceps", "desc")

_muscles = swole.muscles()
_muscles.addMuscle(biceps)


print(_muscles.getMuscle("Biceps").getDescription())