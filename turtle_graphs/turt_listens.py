from turtle import Turtle, Screen
import math, random


pi = math.pi


def flip(self):
    self.left(pi)
def fractional_rotation(self,fraction):
    print(f"rotation by {fraction}")
    self.left(fraction*(2*pi))
Turtle.flip_around = flip
Turtle.fractional_rotation = fractional_rotation

def polygon(self,number_of_sides,side_length,line_type):   
    for step in range(number_of_sides):
        print(step)
        self.line_type = line_type
        self.line_type(self, side_length)
        self.fractional_rotation((1/number_of_sides))

def dashed_forward(self, length):
    while length > 0:
        if length - 10 <= 0:
            self.forward(length)
            length = length - length
        else:
            self.forward(10)
            length = length - 10
        self.up()
        if length - 10 <= 0:
            self.forward(length)
            length = length - length
        else:
            self.forward(10)
            length = length - 10
        self.down()
def ortho_randomize(self):
    direction = (random.randrange(0,3))*(pi/2)
    self.left(direction)
Turtle.ortho_randomize = ortho_randomize
Turtle.dashed_forward = dashed_forward
Turtle.polygon = polygon

turt = Turtle()
turt.shape("turtle")
turt.color("blue")
turt.radians()
def move():
    turt.forward(100)
    print("moving forward")
    # turt.forward(amount)
def fractional_rotation_half(self):
    self.left(pi/2)
def fraction_rotation_right_half(self):
    self.left(3/2*pi)
Turtle.fractional_rotation_half =fractional_rotation_half

Turtle.fractional_right = fraction_rotation_right_half



screen = Screen()
screen.listen()




# turt.onkeypress(moveForward(turt,100))

screen.onkey(move,"space")
screen.onkey(turt.fractional_rotation_half, "a")
screen.onkey(turt.fractional_right, "d")

screen.exitonclick()
