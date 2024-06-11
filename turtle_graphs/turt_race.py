from turtle import Turtle, Screen
import math, random
import random

pi = math.pi



turtBlue = Turtle()
turtGreen = Turtle()

turtBlue.color("blue")
turtGreen.color("green")
turtBlue.shape("turtle")
turtGreen.shape("turtle")

def race(self):
    self.forward(random.choice([1,2,11,10,5,0,3,50]))
Turtle.race = race


screen = Screen()
def reset(turtleArray):
    for turt in turtleArray:
        turt.penup()
    i = 0
    for turt in turtleArray:
        if i % 2 == 0:
            turt.setpos(-(screen.canvwidth/2),i+1*10)
        else:
            turt.setpos(-(screen.canvwidth/2),i+1*-10)
        i += 1
    for turt in turtleArray:
        turt.pendown()

def getXofTurtles(turtleArray):
    positions = []
    for turt in turtleArray:
        positions.append(turt.position())
    return positions
def checkXofTurtles(positionArray, maxX):
    for position in positionArray:
        if position[0] >= maxX:
            return False
        else:
            return True
        

turtleSet = [turtBlue,turtGreen]

def raceTurts(turtles):
    while checkXofTurtles(getXofTurtles(turtles), maxX = (screen.canvwidth)):
        for each in turtles:
            each.race()
    screen.clear()
def racethem():
    raceTurts(turtleSet)

reset(turtleSet)
screen.listen()
screen.onkeypress(racethem, "space")

screen.exitonclick()
