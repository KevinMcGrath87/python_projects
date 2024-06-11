from turtle import Turtle 



# Frog class should establish Frog controls, shape and initialization. 


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.left(90)
        self.shape("turtle")
        self.penup()
    def moveUP(self):
        self.forward(10)    
    