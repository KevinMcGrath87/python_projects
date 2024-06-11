from turtle import Turtle, bye
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREENCOLOR = "black"
SCREENSIZE = [800, 600]



class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.bgcolor(SCREENCOLOR)
        self.screen.setup(*SCREENSIZE)
        
    def drawLine(self):
        pass 

        # what about the dividing line?
        # need to draw it...before updating the drawing.



table = Table()
table.screen.tracer(0)
table.screen.listen()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()
distancex = table.screen.window_width()/2
paddle1.setpos(distancex-40,0)
paddle2.setpos((-distancex)+30,0)
table.screen.update()
gameOn = True
# config
def exeunt(x,y):
    print("exeunt")
    gameOn = False
    bye()
table.screen.onclick(exeunt)    
while gameOn == True:
    # print("updating")
    ball.animate()
    ball.detectCollision(paddle1.pos(), paddle2.pos())
    table.screen.update()
# table.screen.mainloop()




