from turtle import Turtle, Screen
import math, random







# should snake inherit from Turtle..I think sooo
# the snake will have a head position that will be passed down to the next segment of the snake on each frame the head position will be incremented along one of the axes everyframe.
# snakes will be like a binar tree or linked list. they will maintain a head and a tail... upon creation
# segments will be created either as head or tail or will have a super segment and child segment

# need to keep track of segment positions

class Snake:
    def __init__(self, state):
        if(state):
            self.length = state["length"]
            self.alive = True
            self.score = state["score"]
            self.head = state["head"]
            self.tail = state["tail"]
            self.axis = state["axis"]
        else:
            self.length = 3
            self.alive = True
            self.score = 0
            self.axis = 0
    def addSegment(self):
        newSegment = Segment(leads = self.head)
        self.head.follows = newSegment
        newPosition = self.head.position
        if self.axis == 90:
            newPosition[1]= newPosition[1]+20
            newSegment.place(newPosition)
        elif self.axis ==180:
            newPosition[0]= newPosition[0]-20
            newSegment.place(newPosition)
        elif self.axis == 0:
            newPosition[0]= newPosition[0]+20
            newSegment.place(newPosition)
        elif self.axis == 270:
            newPosition[1]= newPosition[1]-20
            newSegment.place(newPosition)
        self.head = newSegment
        self.head.setheading(self.axis)
        segment = self.head
        while(segment):
            segment.position = list(segment.pos())
            segment = segment.leads
        # newSegment.forward(20)
        print(self.head.position)
        self.length += 1
    # def checkStatus(self):
    #     # check for border hit.
    #     currentSegment = self.head.leads
    #     while(currentSegment):
    #         if(self.head.position==currentSegment.position):
    #             # end game
    #             self.alive = False
    #         currentSegment = currentSegment.leads
    #     return self.alive 
    def w(self):
        if not self.axis == 270:
            self.axis = 90  
            self.head.setheading(self.axis) 
    def a(self):
        if not self.axis == 0:
            self.axis = 180
            self.head.setheading(self.axis)
    def d(self):
        if not self.axis == 180:
            self.axis = 0
            self.head.setheading(self.axis)
    def s(self):
        if not self.axis == 90:
            self.axis = 270       
            self.head.setheading(self.axis)  
    def moveSnake(self):
        segment = self.tail
        while(not segment == self.head):
            segment.position = segment.follows.position
            segment.place(segment.position)
            # print(segment.follows.position)
            segment = segment.follows
        self.head.forward(20)
        self.head.position = list(self.head.pos())
    










    # def update(self, segment):
    #     while segment.leads:
    #         segment.leads.place(segment.position)
    #         segment = segment.leads

        # if self.leads and not self.follows:
        #     self.update(self.leads)
        # if self.follows:
        #     self.position = self.follows
        #     if self.leads:
        #         self.update(self.leads)




        


# Tell Turtle’s state
# position() | pos()
# towards()
# xcor()
# ycor()
# heading()
# distance()
# shape()
# resizemode()
# shapesize() | turtlesize()
# shearfactor()
# settiltangle()
# tiltangle()
# tilt()
# shapetransform()
# get_shapepoly()


# class Segment(Turtle):
#     def __init__(self,size=20,shape="square", color="white" ,follows=None, leads=None, position = [0,0]):
#         super().__init__(shape)
#         self.size = size
#         # self.shape = shape
#         self.color = color
#         self.follows = follows
#         self.leads = leads
#         # position attribute inherited from Turtle?
#         self.position = position
    
class Segment(Turtle):
    def __init__(self,size=1,shape="square", colour="green" ,follows=None, leads=None, position = [0,0] ):
        super().__init__(shape)
        self.turtlesize(size) 
        self.penup()
        # self.shape = shape
        self.color(colour)
        self.follows = follows
        self.leads = leads
        self.position = position
        # position attribute inherited from Turtle?
    def place(self,position):
        self.position = position
        self.goto(position)



class Food(Turtle):
    def __init__(self, placement = []):
        super().__init__()
        self.penup()
        self.placement = placement
        self.goto(placement)


# moving the snake. every "frame" the snake will run check state. if the position of the snake head
# equals the position of any snake segment snake runs snake Destroy
# if the snake head position is on the border runs snake destroy.
# if snake state is fine snake moves along direction last specified. i.e. applies forward to head
# the previous position of head is passed to the follower and so on down the line.

# turtle.window_height()
# Return the height of the turtle window.

# >>>
# screen.window_height()
# 480
# turtle.window_width()
# Return the width of the turtle window.

class Game:
    def __init__(self):
        self.screen = Screen()

        self.snake = Snake(state = {})
        self.snake.head = Segment()
        self.snake.tail = self.snake.head
        self.snake.head.place([-20,0])
        self.snake.addSegment()
        self.snake.addSegment()
        self.food = self.placeFood()

    def placeFood(self):

        screenwidth = self.screen.screensize()[0]
        screenheight = self.screen.screensize()[1]
        foodX = random.randint(-(screenwidth/2),screenwidth/2)
        foodY = random.randint(-(screenheight/2),screenheight/2)
        return(Food([foodX,foodY]))
    def moveFood(self):
        screenwidth = self.screen.screensize()[0]
        screenheight = self.screen.screensize()[1]
        foodX = random.randint(-(screenwidth/2),screenwidth/2)
        foodY = random.randint(-(screenheight/2),screenheight/2)
        self.food.goto([foodX,foodY])




    def statusCheck(self):

        snakeX= self.snake.head.position[0]
        snakeY =self.snake.head.position[1]
        corners = list(self.screen.screensize())
        for x in corners:
            x = x/2
        snakeDistX = abs(snakeX)+10
        snakeDistY = abs(snakeY)+10
        if(abs(snakeDistX - corners[0])<=10):
            self.snake.alive = False
            self.screen.bye()
        if(abs(snakeDistY - corners[1])<=10):
            self.snake.alive = False
            self.screen.bye()
        if abs(snakeX - self.food.pos()[0])<= 10 and abs(snakeY - self.food.pos()[1]) <= 10:
            self.snake.addSegment()
            self.moveFood()
        segment = self.snake.head.leads     
        while(segment):
            if(abs(self.snake.head.position[0]-segment.position[0])<=0 and abs(self.snake.head.position[1]-segment.position[1]<=0)):
                self.screen.bye()
            segment = segment.leads    

        # self.snake.head.setheading(self.snake.axis)

        
        # self.snake.head.colour = "blue"

        # print(self.snake.head.pos())
        # shead.leads = Segment(position = [0,0])
        # body = shead.leads
        # body.place([0,0])
        # print(self.snake.head.leads.pos())
        # body.leads = Segment(position = [-20,0])
        # tail = body.leads
        # tail.place([-20,0])

        # self.snake.head.leads = Segment(position = [0,0])
        # self.snake.head.leads.leads = Segment(position=[-20,0])
        # screen = Screen()
        # screen.listen()
        # screen.mainloop()

    def runGame(self):
            screen = self.screen
            screen.listen()
            screen.onkey(self.snake.w, "w")
            screen.onkey(self.snake.a, "a")
            screen.onkey(self.snake.s, "s")
            screen.onkey(self.snake.d, "d")
            while (self.snake.alive):
                # screen.tracer(10,10)
                self.snake.moveSnake()
                self.statusCheck()


            # self.snake.a()
            # self.snake.a()

            # i = 0
            # while(i<100):
            #     self.snake.head.fd(30)
            #     self.snake.head.right(45)
            #     self.snake.head.fd(50)
            #     self.snake.update(segment = self.snake.head)
            #     i += 1


            screen.exitonclick()
            # self.snake.update(self.snake.head)
            # print("update")


game = Game()


game.runGame()






    # def makeSnake():
    #     # screen = Screen()
    #     # screen.listen()
    #     # screen.onkey()
    #     head = Segment(position = [20,0])
    #     tail = Segment(position = [0,0])
    #     body = Segment(position = [-20,0])
    #     body.follows = head
    #     body.leads = tail
    #     tail.follows = body
    #     head.leads = body
    #     snake = Snake(state = {})
    #     snake.headPosition = head.pos()
    #     snake.head = head
    #     snake.tail = tail
    #     print(head.turtlesize())
    #     print(head.width())