from turtle import Turtle, Screen
from frog import Frog
from car import Car
import random, time

ROADY = 350
ROADX = 450
SPEED = 20


# Highway class should control establishing the screen, rendering elements, refreshing and controlling elements, updating score, reseting and ending the game.
class Highway(Turtle):
    def __init__(self):
        # super().__init__()
        self.screen = Screen()
        self.froggy = Frog()
        self.screen.tracer(0)
        self.makeScreen(ROADY=ROADY, ROADX=ROADX)
        self.cars = []
    def makeScreen(self, ROADY, ROADX):
        self.screen.screensize(ROADX, ROADY)
        print("made Screen")
    def makeCars(self):
        number = random.randint(0 , 6)
        for _ in range(number):
            self.cars.append(Car()) 
    def moveCars(self):
        for car in self.cars:
            car.forward(SPEED)


# initialize game
highway = Highway()
highway.froggy.setpos(0, -(ROADY-((ROADY/2)-50)) )
highway.makeCars()
# highway.screen.listen()
GAME = True
while GAME == True:
    generate = random.random()
    if generate >= .5 :
        highway.makeCars()
    highway.moveCars()
    highway.screen.update()
    time.sleep(.25)
    
    

# highway.cars.append(Car())
# highway.cars.append(Car())
# highway.cars.append(Car())
# highway.cars.append(Car())
# for car in highway.cars:
#     car.setpos(-50,30)

highway.screen.mainloop()


