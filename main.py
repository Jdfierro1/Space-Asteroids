import os
import random
import turtle 

#Required by MacOS to show window 
turtle.fd(0) 
#Set the animations speed to max 
turtle.speed(0)
#Change the background color 
turtle.bgcolor("black")
#Hide default turtle
turtle.ht() 
#Save memory 
turtle.setundobuffer(1)
#This speeds up drawing 
turtle.tracer(1) 

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

player = Sprite("triangle", "white", 0 ,0)

turtle.done()
#delay = raw_input("Press enter to finish. >")