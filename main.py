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

    def move(self):
        self.fd(self.speed)

        ######################
        # Boundary Detection # 
        ######################

        if self.xcor() > 299: 
            self.setx(299)
            self.rt(180)
        if self.xcor() < -299:
            self.setx(-299) 
            self.rt(180)
        if self.ycor() > 299: 
            self.sety(299)
            self.rt(180)
        if self.ycor() < -299:
            self.sety(-299) 
            self.rt(180)

# Player class which inherits from the Sprite class
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        #Lets make the player a little faster than the default Sprite
        self.speed = 4
        #####
        # lives has not been established yet, need to revisit this
        #####
        self.lives = 3

#####################
# Movement Methods  #
#####################

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Game():
    def __init__(self):
        self.level = 1 
        self.score = 0 
        self.state = "Playing"
        self.pen = turtle.Turtle()
        self.lives = 3 

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#Create the Game 
game = Game()
game.draw_border()

#Create The Player
player = Player("triangle", "white", 0 ,0)

#####################
# Keyboard Bindings #
#####################
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()




#Main Game Loop 
while True:
    # Player moves forward at speed of 1 as initialized in the Sprite class
    player.move()
    #player.turn_left()

turtle.done()
#delay = raw_input("Press enter to finish. >")