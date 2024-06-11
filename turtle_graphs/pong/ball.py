from turtle import Turtle, Screen


SPEED = .5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(10)
        self.shape("circle")
        self.setposition(0,0)
        self.color("white")
        self.penup()
    def animate(self):
        self.forward(SPEED)
    def detectCollision(self, paddle1Position, paddle2Position):
        ballBox = [*self.pos()]
        paddle1X = paddle1Position[0]
        paddle1Y = paddle1Position[1]
        paddle2X = paddle2Position[0]
        paddle2Y = paddle2Position[1]
        # print(f'ball@ {ballBox} paddle1x {paddle1X} paddle1 y {paddle1Y}')

        if((ballBox[0]+10 >= paddle1X-10) and ((ballBox[1] <= paddle1Y+40 ) and (ballBox[1] >= paddle1Y-40))):
            self.setheading(180-self.heading())
            print("collision")
        elif (ballBox[0]-10 <= paddle2X+10 and ((ballBox[1] <= paddle2Y+40) and (ballBox[1] >= paddle2Y-40))):
            self.setheading(180-self.heading())
            print("collision")

        # get positions of paddles...


