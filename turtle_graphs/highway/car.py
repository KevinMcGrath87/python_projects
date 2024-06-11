from turtle import Turtle
import random



COLORS = ['red', 'green','blue','yellow','orange','pink']


random.randint(0, 2)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0,len(COLORS)-1)])
        self.shape('square')
        self.shapesize(1,3)
        self.left(180)
        self.penup()
        self.setpos((self.screen.screensize()[0]/2)+200,random.random()*self.screen.screensize()[1]-self.screen.screensize()[0]/2)