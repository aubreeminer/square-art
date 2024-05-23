
#import the turtle library in order to create a canvas
from turtle import *

#import random integer capability
from random import randint

speed (0)

bgcolor('black')

x = 1

#400 is the number of rotations 
while x < 400:
    #generate random variations from hex colors
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
#generate the color of the pen from the above values
    pencolor(r,g,b)

    fd(50 + x)
    rt(90.911)
#iterates x + 1 until x = 399
    x = x+1
exitonclick()
#user may click on canvas when complete
