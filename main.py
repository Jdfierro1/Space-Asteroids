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

######################
#     Sprite Class   # 
######################

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
            self.rt(90)
        if self.xcor() < -299:
            self.setx(-299) 
            self.rt(90)
        if self.ycor() > 299: 
            self.sety(299)
            self.rt(90)
        if self.ycor() < -299:
            self.sety(-299) 
            self.rt(90)

    ######################
    # Collission Detection # 
    ######################
    def is_collission(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and (self.xcor() <= (other.xcor() + 20)) and (self.ycor() >= (other.ycor() - 20)) and (self.ycor() <= (other.ycor() + 20)):
            return True
        else: 
            return False

#####################
#   Player Class    #
#####################

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=1, stretch_len=0.6, outline=3)  # 3-pixel outline width
        self.setheading(random.randint(0,360))
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

#####################
#   Enemy Class     #
#####################

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # Enemy is faster than the player and sprite by default
        self.speed = 6
        self.setheading(random.randint(0,360))

#####################
#   Allies Class     #
#####################

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=1, stretch_len=0.6, outline=3)  # 3-pixel outline width
        self.speed = 8
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(self.speed)

        ######################
        # Boundary Detection # 
        ######################

        if self.xcor() > 299: 
            self.setx(299)
            self.lt(90)
        if self.xcor() < -299:
            self.setx(-299) 
            self.lt(90)
        if self.ycor() > 299: 
            self.sety(299)
            self.lt(90)
        if self.ycor() < -299:
            self.sety(-299) 
            self.lt(90)

#####################
#   Missile Class   #
#####################

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 20 
        self.shapesize(stretch_wid=0.05, stretch_len=0.6, outline=3)  # 3-pixel outline width
        self.color("yellow", "white") 
        self.status = "ready"
        self.goto(-1000, 1000)
    
    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        
        if self.status == "firing":
            self.fd(self.speed)
        
        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() <-290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

#####################
#   Game Class      #
#####################

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

##########################
# Create Class Variables #
##########################

game = Game()
game.draw_border()
player = Player("triangle", "orange", 0 ,0)
enemy = Enemy("circle", "red", random.randint(0, 360), random.randint(0, 360))
ally = Ally("triangle", "blue", random.randint(0, 360), random.randint(0, 360))
missile = Missile("square", "yellow", 0, 0)

#####################
# Keyboard Bindings #
#####################

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main Game Loop 
while True:
    player.move()
    enemy.move()
    missile.move()
    ally.move()

    #Check for a space ship collission
    if player.is_collission(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        player.speed = 1
        enemy.goto(x, y)

    # Check for a missile collission 
    if missile.is_collission(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        missile.status = "ready"
    
    #CHeck for ally collission with player 
    if player.is_collission(ally):
        ally.setheading(random.randint(-250, 250))
        
#delay = raw_input("Press enter to finish. >")