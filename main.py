##By HIMANSHU PANDEY

import tkinter as tk
import random

colors = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0

timeleft = 60 #initial time

def startGame(event):
    if timeleft == 60:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set() #making the text box active
        if e.get().lower() == colors[1].lower():
            score += 10
        e.delete(0,tk.END)
        random.shuffle(colors)
        label.config(fg = str(colors[1]),text = str(colors[0].lower()))
        scoreLabel.config(text = "Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000,countdown) #run the function again after 1 seconds


############################################################################################
root = tk.Tk()
root.title("Game Of Colors")
root.geometry("400x400")

instructions =  tk.Label(root,text = "Type the color not the word!",font = ('Helvetica',12))
instructions.pack()

scoreLabel = tk.Label(root,text = "Press enter to start", font = ('Helvetica',12,'bold'))
scoreLabel.pack(ipady = 5)

timeLabel = tk.Label(root,text = "Time left: " + str(timeleft), font = ('Helvetica',12))
timeLabel.pack(ipady = 10)

label = tk.Label(root, font = ('Helvetica',60))
label.pack(pady = 50)

e = tk.Entry(root)

root.bind('<Return>',startGame)
e.pack(ipady = 5)

e.focus_set() #set focus to the entry box


root.mainloop()
