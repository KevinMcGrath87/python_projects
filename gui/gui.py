import tkinter
import tkinter.ttk
import numpy
import math
import time
from PIL import Image, ImageDraw, ImageTk, PSDraw
import os

window = tkinter.Tk()
maxWidth = window.winfo_screenwidth()
maxHeight = window.winfo_screenheight()
window.title('first of its kind')

window.minsize(maxWidth-100,maxHeight-100)


name = tkinter.Label(text = 'HI', font=('arial',24,'bold'))


name.config(background='blue')
name.pack(side = 'top')


x = 0
windowWidth = 1000
windowHeight = 500
canvas = tkinter.Canvas(window,width=windowWidth, height=windowHeight,background='white')
canvas.pack()

# distance = 0
# alter phase and redraw.
# # function to calculate x value of line.
# while x < windowWidth:
#     if x == 0:
#         canvas.create_line(0,0, 0,500, width = 4, fill = 'red')
#     else:
#         distance = distance + 3*abs((math.sin(x)-math.sin((x-1))))
#         canvas.create_line(distance,0, distance,500,width = 1, fill = 'red')
#     x += 1

def sinPlot(phase, scale=3,lineColor = 'blue',lineWidth = 1,canvas=canvas ):
    distance = 0
    x = 0
    while x < windowWidth:
        if x == 0:
            canvas.create_line(0,0, 0,500, width = lineWidth, fill = lineColor)
        else:
            lineWidth = scale*(.5*(math.sin(x))+.51)
            distance = distance + scale*abs((math.sin(x+phase)-math.sin((x-1+phase))))
            canvas.create_line(distance,0, distance,500,width = lineWidth, fill = lineColor)
        x += 1
def sinPlot2(phase,scale = 1, lineColor = 'blue',lineWidth = 1,canvas=canvas ):
    for x in range(0,windowWidth,scale):
            lineWidth = int(scale*(.5*(math.sin((x+phase)))+.5))
            canvas.create_line(x,0, x,500,width = lineWidth, fill = lineColor)
def sinPlot3(phase,scale = 1, lineColor = 'blue',lineWidth = 1,canvas=canvas ):
    for x in range(0,int(windowWidth/2)+1,scale):
            lineWidth = ((scale-1)*(.5*(math.sin((x+phase)))+.5))
            lineColor = rgbFunct((.5*(math.sin((x+phase*2)))+.5))
            # canvas.config(background=rgbFunct(.5*(math.cos((x+phase*.35)))+.5))
            canvas.config(background='black')
            canvas.create_line(x,0, x,500,width = lineWidth, fill = lineColor)
            canvas.create_line(windowWidth-x,0,windowWidth-x,500, width=lineWidth, fill = lineColor)
def rgbFunct(number):
    if number >= 0 and number < 1/3:
        number = number*255*3.0
        rgb = (int(number), 0 , 255)
    elif number >= 1/3 and number < 2/3:
        number = ((number*3.0)-1)*255
        rgb = (255,0,int(number))
    elif number >= 2/3 and number <=1:
        number = ((number*3.0)-2)*255
        rgb= (255,int(number),0)
    r,g,b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'




# def animateSin(phase=0,speed = .0005):
#     while True:
#         canvas.delete("all")
#         # sinPlot(phase=phase, scale = 10)
#         # sinPlot2(phase,scale = 25)
#         sinPlot3(phase, scale = 25)
#         phase +=.009
#         time.sleep(speed)
#         canvas.update()
    


# def animateSin(phase=0,speed = .0005,frames, duration, num_frames):
#     frame_number = 0
#     while frame_number <= num_frames:
#         canvas.delete("all")
#         # sinPlot(phase=phase, scale = 10)
#         # sinPlot2(phase,scale = 25)
#         sinPlot3(phase, scale = 25)
#         phase +=.009
#         time.sleep(speed)
#         canvas.update()
#         canvas.postscript(file = 'screen_anime.ps')
#         frame = Image.open('screen_anime.ps')
#         # may need to add a crop to canvas here...
#         frames.append(frame)
#         frame_number += 1
#     frames[0].save('anime_gif', save_all = True, )   

frames = []
duration = 10
num_frames = 4

def animateSin(frames, duration, num_frames, phase=0,speed = .05):
    frame_number = 0
    while frame_number < num_frames:
        canvas.delete("all")
        # sinPlot(phase=phase, scale = 10)
        # sinPlot2(phase,scale = 25)
        sinPlot3(phase, scale = 25)
        phase +=.009
        canvas.update()
        # PSDraw.PSDraw('animated.ps')
        # PSDraw.PSDraw.begin_document()
        canvas.postscript(file = 'screen_anime.ps')
        frame = Image.open('screen_anime.ps')
        # may need to add a crop to canvas here...
        frames.append(frame)
        print(len(frames))
        frame_number += 1
        time.sleep(speed)
    print(len(frames), "frames in frames")    
    frames[0].save('anime.gif', save_all = True,append_images=frames[1:],duration=duration, loop = 0 )
    print('file should be saved now')


        

animateSin(frames, duration, num_frames)


# window.update()

tkinter.mainloop()






























# argList = ['kevin','2',2, 'mcgrath']

# def killIt(*args):
#     for x in args:
#         if type(x) == str:
#             print(x)
#         else:
#             print('not a string')


# killIt(*argList)