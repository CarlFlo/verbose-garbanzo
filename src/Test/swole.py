class Routine:
    def __init__(self):
        pass

    def showRoutine(self):
        pass

class Split:
    def __init__(self):
        pass

class muscle:
    
    def __init__(self, name,desc):
        self.name = name
        self.desc = desc

    def description(self, desc):
        print(self.desc)
        
biceps = muscle(biceps,"The biceps, also biceps brachii (Latin for two-headed muscle of the arm), is a large muscle that lies on the front of the upper arm between the shoulder and the elbow. Both heads of the muscle arise on the scapula and join to form a single muscle belly which is attached to the upper forearm. While the biceps crosses both the shoulder and elbow joints, its main function is at the elbow where it flexes the forearm and supinates the forearm. Both these movements are used when opening a bottle with a corkscrew: first biceps unscrews the cork (supination), then it pulls the cork out (flexion).")
quadriceps = muscle(quadriceps,"The quadriceps femoris (/ˈkwɒdrɪsɛps ˈfɛmərɪs/, also called the quadriceps extensor, quadriceps or quads) is a large muscle group that includes the four prevailing muscles on the front of the thigh.It is the great extensor muscle of the knee, forming a large fleshy mass which covers the front and sides of the femur. The name derives from Latin four-headed muscle of the femur.")
class muscles:

    _muscles = {}

    def addMuscle(self, name):
        self._muscles[name]

    def getMuscle(self,name):
        return self._muscles[name]


class exercise:

    def __init__(self, name, muscle):
        self.name = name
        self.name = muscle  # hämta från muscles klassen


class exercises:

    _exercises = {}

    def addExercise(self, exercise):
        pass