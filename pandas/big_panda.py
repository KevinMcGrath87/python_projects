import pandas as pd
import numpy as np
import csv


data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data = pd.DataFrame(data)
print(data.keys())
print(data['Primary Fur Color'].head(50))


colorMap = {
    "gray": 0,
    "cinn":0,
    "black":0,
}


for color in data['Primary Fur Color']:
    if color == 'Gray':
        colorMap['gray'] += 1
    if color == 'Black':
        colorMap['black'] += 1
    if color == 'Cinnamon':
        colorMap['cinn']+= 1
    else:
        continue


colorMap = {
    'colors': ['gray','black','cinnamon'],
    'number': [colorMap['gray'],colorMap['black'],colorMap['cinn']]
}
print(colorMap)
colorCounts = pd.DataFrame(colorMap)
print(colorCounts)

# dfGray = pd.DataFrame(data['Primary Fur Color'][data['Primary Fur Color']=='Gray'])
# for gray in dfGray:
#     colorMap['gray']+1
# print(dfGray.head(20))


# print(data.head(10))

