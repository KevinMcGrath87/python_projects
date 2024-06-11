from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
# PATH = 'score.txt'

PATH = os.fspath('G:/code/py_projects/turtle_graphs/snake/score.txt')
absPath = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(absPath, 'score.txt')
absPath = PATH
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        print(absPath)
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def get_high_score(self):
        # clarify reading and writing
        # text = os.read(PATH)
        with open(PATH, "r") as current:
            current = current.read()
            print (current)
            current = int(current)
            if current:
                self.high_score = current
    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(PATH, "w") as hs:
                print("writing high score")
                hs.write(str(self.high_score))

        # if self.score > self.high_score:
        pass
    def reset(self):
        self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.get_high_score()
        self.write(f"Score: {self.score} High: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
