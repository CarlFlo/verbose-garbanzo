from turtle import *

speed(0)
color('red', 'yellow')
begin_fill()
leftplus = 170
forwardplus = 200

i = 0

while True:
    forward(forwardplus) #200
    left(leftplus) #170
    leftplus += 1
    forwardplus -= 1
    i += 1

    for n in range(150):
        pass

    if abs(pos()) < 1 or i > 150:
        break

    print(i)
   

#end_fill()
done()
