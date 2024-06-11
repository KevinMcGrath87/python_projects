from turtle import Turtle, Screen
PADDLECOLOR = 'blue'
PADDLESIZE = [1,4]




class Paddle(Turtle):
    def __init__(self,player):
        super().__init__()
        self.screen = Screen()
        self.movingFlag = False
        self.color(PADDLECOLOR)
        self.shape("square")
        self.shapesize(PADDLESIZE[0],PADDLESIZE[1])
        self.penup()
        self.setheading(90)
        self.screen.listen()
        self.player = player
        self.keys = [["w","s"],["e","d"]]
        if self.player == 1:
            self.playKeys = self.keys[0]
        else:
            self.playKeys = self.keys[1] 
        self.screen.onkeypress(self.up, self.playKeys[0])
        self.screen.onkeypress(self.down, self.playKeys[1])
        # self.screen.onkeyrelease(self.stop , "w")
        # self.screen.onkeyrelease(self.stop, "s")

    def up(self):
        print("moving up!", self.movingFlag)
        # self.movingFlag = True
        # while self.movingFlag:
        if not (self.ycor()) >= (self.screen.screensize()[1]/2):
                self.setheading(90)
                self.forward(15)
                print(self.ycor(), self.screen.screensize()[1]/2)
                # self.screen.update()
    def down(self):
        # self.movingFlag = True
        # while self.movingFlag:
            if not (self.ycor()) <= -(self.screen.screensize()[1]/2):
                    self.setheading(270)
                    self.forward(15)
                    print(self.ycor(), -self.screen.screensize()[1]/2)
                    # self.screen.update()







# paddle = Paddle()

# paddle.screen = Screen()

# paddle.screen.exitonclick()