from turtle import Turtle, Screen
import math, random
from prettytable import PrettyTable

pi = math.pi


turt = Turtle()
turt.shape("turtle")
turt.color("blue")
turt.radians()
def flip(self):
    self.left(pi)
def fractional_rotation(self,fraction):
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

# for x in range(3, 12):
#     turt.polygon(x, x*2, dashed_forward)
# turt.fractional_rotation(1/13)
# turt.polygon(4, 110, dashed_forward)
# turt.fractional_rotation(1/13)
# turt.polygon(5, 207, dashed_forward)
# turt.fractional_rotation(1/13)
# turt.polygon(6, 33, dashed_forward)

# steps = 0
# while steps < 200 :
#     turt.ortho_randomize()
#     turt.forward(50)
#     steps+=1

for step in range(0, 100):
    turt.fractional_rotation(step/100)
    turt.circle(25)

screen_1 = Screen()
print(screen_1.canvheight)

screen_1.exitonclick()






