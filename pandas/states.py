from turtle import Turtle, Screen
import pandas as pd

stateData = pd.read_csv('50_states.csv')


screen = Screen()

screen.title('u.s. state game')

image = 'blank_states_img.gif'
screen.addshape(image)


turt = Turtle()
turt.shape(image)
turt2 = Turtle()
states = []
while(len(states) < 50):
        
    answer = screen.textinput('Guess a State','Guess a state')
    # locationX = (stateData['x'][stateData['state']== answer])
    # locationY = (stateData['y'][stateData['state']== answer])
    # locationX = int(locationX.iloc[0])
    # LocationY = int(locationY.iloc[0])
    # print('x loc', locationX)
    # print('y loc', locationY)
    if answer in stateData['state'].tolist() and not (answer in states):
        stateRow = stateData[stateData['state'] == answer]
        x = (stateRow['x'].tolist()[0])
        y = (stateRow['y'].tolist()[0])
        # turt.goto(stateData['x'].astype(float),stateData['y'].astype(float))
        turt2.goto(x,y)
        turt2.write(answer)
        states.append(answer)
    # turt.goto(locationX,locationY)
    # turt.write('answer')
    screen.update()

screen.mainloop()