'''Snake'''
#imports everything needed
from tkinter import *
import random
import time

#Initalises the canvas
Box = Tk()
Frame = Canvas(Box, height = 500, width = 500, bg = "grey")

Box.tk.call('wm', 'iconphoto',Box._w, PhotoImage(file='Logo.gif'))
Box.wm_title("Snake")
ScoreBox = Text(Box, height = 2, width = 50)

#Creates the varibles that will store the game
Grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
Snake = [[0,0]]
head = [0,0]
start = time.time()
over = False
direction = "down"
found = False


#Testing code
def printGrid():
    global Grid
    for i in Grid:
        print(i)
    print("\n\n")

#-----Food-----#
#Checks to see if there is food on the grid
def food():
    for i in range(0, len(Grid)):
        for a in range(0, len(Grid[i])):
            if Grid[i][a] == 2:
                return True
    return False

#Places food if there is no food on the grid    
def foodPlace():
    while not food():
        x = random.randint(1,18)
        y = random.randint(1,18)
        if Grid[x][y] == 0:
            Grid[x][y] = 2
            found = False
            break
            

#-----Movement functions-----#
def Up():
    global over                                                         #Allows the system to know if the game is over
    Grid[head[1]][head[0]] = 1                                          #Sets the currecnt location of the head to be a body square
    try:
        if Grid[head[1]-1][head[0]] == 2:Snake.append(Snake[len(Snake)-1])  #Checks to see if the game snake has "eatten" and duplicats the last value in the snake list
    except:return 1
    Snake.insert(0, head[:])                                            #The body of the snake gains the coords of the old head
    Snake.pop()                                                         #The oldest item in the snake is destroyed
    head[1] -= 1                                                        #Changes the poistion of the head
    if head[1] == -1:over = True                                         #Checks to see if this action will move it off the board and then stops the game if it does
    try:                                                                #Start of the try condition
        if Grid[head[1]][head[0]] == 1:over = True                      #If the snake has run into itself, game over                                 
        Grid[head[1]][head[0]] = 3                                      #Tells the grid the position of the new head
    except:return 1                                                     #End of the try condition
    gridShow()                                                          #Updates the grid
    
def Down():
    global over
    Grid[head[1]][head[0]] = 1
    try:
        if Grid[head[1]+1][head[0]] == 2:Snake.append(Snake[len(Snake)-1])
    except:return 1
    Snake.insert(0, head[:])
    Snake.pop()
    if head[1]+1 == 20:over = True
    head[1] += 1
    try:
        if Grid[head[1]][head[0]] == 1:over = True
        Grid[head[1]][head[0]] = 3
    except:return 1
    gridShow()
    
def Right():
    global over
    Grid[head[1]][head[0]] = 1
    try:
        if Grid[head[1]][head[0]+1] == 2:Snake.append(Snake[len(Snake)-1])
    except: return 1
    Snake.insert(0, head[:])
    Snake.pop()
    head[0] += 1
    if head[0] == 20:over = True
    try:
        if Grid[head[1]][head[0]] == 1:over = True
        Grid[head[1]][head[0]] = 3
    except:return 1
    gridShow()
    
def Left():
    global over
    Grid[head[1]][head[0]] = 1
    try:
        if Grid[head[1]][head[0-1]] == 2:Snake.append(Snake[len(Snake)-1])
    except:return 1
    Snake.insert(0, head[:])
    Snake.pop()
    head[0] -= 1
    if head[0] == -1:over = True
    try:
        if Grid[head[1]][head[0]] == 1:over = True
        Grid[head[1]][head[0]] = 3
    except:return 1
    gridShow()
            
#Changes the direction of movement in response to user input
def r(event):   
    global direction
    direction = "right"
def l(event):
    global direction
    direction = "left"
def u(event):
    global direction
    direction = "up"
def d(event):
    global direction
    direction = "down"

#Moves the snake every 1/8 second
def autoMove():
    if over == False:
        foodPlace()
        global direction
        if direction == "left":Left()
        elif direction == "right":Right()
        elif direction == "up":Up()
        elif direction == "down":Down()
        Frame.after(125, autoMove)
    else:
        L1 = "Snake size: " + str(len(Snake))
        L1 = " "*int((50-len(L1))/2) + L1 + " "*int((50-len(L1))/2)
        L2 = "Time lasted: " + str(round(time.time()-start, 1)) + " seconds"
        L2 = " "*int((50-len(L2))/2) + L2 + " "*int((50-len(L2))/2)
        TEXT = L1 + "\n" + L2
        ScoreBox.delete("1.0", END)
        ScoreBox.insert(END, TEXT)
#        print("Snake size: " + str(len(Snake)) + "\nTime lasted: " + str(time.time()-start))

def Play(event):
    global Grid
    global Snake
    global head
    global start
    global over
    global direction
    global found
    Grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    Snake = [[0,0]]
    head = [0,0]
    start = time.time()
    over = False
    direction = "down"
    found = False
    ScoreBox.delete("1.0", END)
    ScoreBox.insert(END, "Snake")
    Frame.after(250, autoMove)

    
Frame.bind('<Up>', u)
Frame.bind('<Down>', d)
Frame.bind('<Right>', r)   
Frame.bind('<Left>', l)
Frame.bind('<space>', Play)

#-----Grid Creation-----#
def gridShow():
    Frame.delete("all")
    for i in range(0, len(Grid)):
        for a in range(0, len(Grid)):       #Loops though the grid
            if Grid[a][i] == 1:         
                if [i,a] not in Snake:      #Checks to see if all of the coords in the grid are meant to be a snake
                    Grid[a][i] = 0
    for i in range(0, len(Grid)):
        for a in range(0, len(Grid[i])):    #Creates the new grid
            if Grid[i][a] == 1:Frame.create_rectangle(a*25, i*25, (a*25)+25, (i*25)+25, fill = "blue")      #Body
            elif Grid[i][a] == 2:Frame.create_rectangle(a*25, i*25, (a*25)+25, (i*25)+25, fill = "green")   #Food
            elif Grid[i][a] == 3:Frame.create_rectangle(a*25, i*25, (a*25)+25, (i*25)+25, fill = "yellow")  #Head




#---------TO DO----------#
#Error testing



ScoreBox.insert(END, "Welcome to Snake")
Frame.after(250, autoMove)
Frame.focus_set()
ScoreBox.pack()
Frame.pack()
Box.mainloop()
