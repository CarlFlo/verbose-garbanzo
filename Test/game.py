import threading
import time
import turtle
import keyboard
import random as rand

wn = turtle.Screen()
wn.setup(360,480)

wn.bgcolor("lightgray")
wn.listen()

windowX = wn.screensize()[0]
windowY = wn.screensize()[1]
windowPadding = 20

exitFlag = 0


class drawObj():
    def __init__(self, num, color, speed, turnSpeed, turnL, turnR):

        rand.seed(num*(time.time()+num)*(num*time.time()))

        self.color = color
        self.size = 5
        self.X = self.randomPosX()
        self.Y = self.randomPosY()
        self.heading = self.randomHeading()
        self.speed = speed
        self.turnSpeed = turnSpeed

        self.turnL = turnL
        self.turnR = turnR

    def randomPosX(self):
        return rand.randint(windowPadding, windowX-windowPadding)

    def randomPosY(self):
        return rand.randint(windowPadding, windowY-windowPadding)

    def randomHeading(self):
        return rand.randint(0, 360)


class myThread (threading.Thread):
    def __init__(self, threadID, name, obj):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.obj = obj

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.obj)
        print("Exiting " + self.name)


def print_time(threadName, obj):
    t = turtle.Turtle()
    t.penup()
    t.color(obj.color)
    t.pensize(obj.size)
    t.speed(0)
    t.setx(obj.X)
    t.sety(obj.Y)
    t.setheading(obj.heading)
    #t.speed(obj.speed)
    t.pendown()

    while exitFlag == 0:

        if rand.randint(0,100) < 50:
            t.penup()
        else:
            t.pendown()

        wn.onKey(t.left(obj.turnSpeed), obj.turnL)
        wn.onKey(t.right(obj.turnSpeed), obj.turnR)

        t.forward(obj.speed)

    threadName.exit()


obj1 = drawObj(1, "red", 3, 10, "a", "s")
obj2 = drawObj(2, "yellow", 3, 10, "k", "l")

# Create new threads
thread1 = myThread(1, "Thread-1", obj1)
thread2 = myThread(2, "Thread-2", obj2)

# Start new Threads
thread1.start()
thread2.start()

wn.exitonclick()

thread1.join()
# thread2.join()
print("Exiting Main Thread")
