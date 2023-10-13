#Import tkinter which is used to create a GUI app
import tkinter as tk
from random import randint
from tkinter import messagebox

#Define required variables
root = tk.Tk()
height = 400
width = 400
secheight = 400/4
secwidth = 400/4
values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Set the application title, size and disable resizing
root.title("2048")
root.geometry("400x500")
root.resizable(False,False)

#Define the canvas varaiable
canvas = tk.Canvas(root, width=width, height=height, bg="lightgrey")
def draw_canvas():
    global canvas
    #Draw verticle lines and horizontal lines
    fill = "black"
    for x in range(4):
        canvas.create_line(secwidth*x, height, secwidth*x, 0, fill=fill)
        canvas.create_line(0, secheight*x, width, secheight*x, fill=fill)
draw_canvas()

#Draw starting numbers 
for x in range(3):
    y = randint(0,3)
    xx = randint(0,3)
    while values[y][xx] == 2:
        y = randint(0,3)
        xx = randint(0,3)
    values[y][xx] = 2
    if xx == 0 and y == 0:
        canvas.create_text(secheight/2, secwidth/2, text='2', fill='black', font=('Arial 25 bold'))
    elif xx == 0:
        canvas.create_text(secheight/2, (secwidth*y)+(secwidth/2), text='2', fill='black', font=('Arial 25 bold'))
    elif y == 0:
        canvas.create_text((secheight*xx)+(secheight/2), secwidth/2, text='2', fill='black', font=('Arial 25 bold'))
    else:
        canvas.create_text((secheight*xx)+(secheight/2), (secwidth*y)+(secwidth/2), text='2', fill='black', font=('Arial 25 bold'))
canvas.pack()

#Update canvas and add a new 2 in a empty square
def update_canvas():
    global canvas
    #Check if there is a empty square
    contains_zero = any(any(value == 0 for value in row) for row in values)
    if contains_zero == False:
        messagebox.showinfo("Message","Game Over!")
    elif contains_zero == True:
        #Remove tbe current canvas
        canvas.destroy()
        #Create a new canvas
        canvas = tk.Canvas(root, width=width, height=height, bg="lightgrey")
        #Draw the grid
        draw_canvas()
        #Add a new 2 to the values array
        yy = randint(0,3)
        xx = randint(0,3)
        while values[yy][xx] != 0:
            yy = randint(0,3)
            xx = randint(0,3)
        values[yy][xx] = 2
        #Draw the values
        for y in range(len(values)):
            for x in range(len(values[y])):
                #If the value equals zero, replace it with ''
                current = values[y][x] if values[y][x] != 0 else ''
                #Draw the values onto the canvas
                if x == 0 and y == 0:
                    canvas.create_text(secheight/2, secwidth/2, text=current, fill='black', font=('Arial 25 bold'))
                elif x == 0:
                    canvas.create_text(secheight/2, (secwidth*y)+(secwidth/2), text=current, fill='black', font=('Arial 25 bold'))
                elif y == 0:
                    canvas.create_text((secheight*x)+(secheight/2), secwidth/2, text=current, fill='black', font=('Arial 25 bold'))
                else:
                    canvas.create_text((secheight*x)+(secheight/2), (secwidth*y)+(secwidth/2), text=current, fill='black', font=('Arial 25 bold'))
        #Output the canvas
        canvas.pack()
            

#Define function for when a button is clicked
def btn_clicked(t):
    for a in range(3):
        for y in range(4):
            #Create a new array with the affected values
            row = []
            for x in range(4):
                if t == 'Left' or t == 'Right':
                    if values[y][x] != 0:
                        row.append(values[y][x])
                elif t == 'Up' or t == 'Down':
                    if values[x][y] != 0:
                        row.append(values[x][y])
            if t == 'Right' or t == 'Down':
                row.reverse()
            #Add values that are next to each other and equal to each other
            if len(row) > 1:
                for x in range(len(row)-1):
                    if row[x] == row[x+1]:
                        row[x] += row[x+1]
                        row[x+1] = 0
            #Ensure the array contains 4 values
            if len(row) == 0:
                row = [0,0,0,0]
            elif len(row) == 1:
                row = [row[0],0,0,0]
            elif len(row) == 2:
                row = [row[0], row[1], 0, 0]
            elif len(row) == 3:
                row.append(0)
            #Add row values back to values array
            if t == 'Left' or t == 'Right':
                if t == 'Right':
                    row.reverse()
                values[y] = row
            elif t == 'Up' or t == 'Down':
                if t == 'Down':
                    row.reverse()
                values[0][y] = row[0]
                values[1][y] = row[1]
                values[2][y] = row[2]
                values[3][y] = row[3]
        #Update canvas        
        update_canvas()

#Draw buttons
t = 'Left'
btn = tk.Button(root, text = 'Left', command=lambda t='Left':btn_clicked(t), height=2, width=10).place(x=70,y=452)
btn = tk.Button(root, text = 'Up', command=lambda t='Up':btn_clicked(t), height=2, width=10).place(x=150,y=410)
btn = tk.Button(root, text = 'Down', command=lambda t='Down':btn_clicked(t), height=2, width=10).place(x=150,y=452)
btn = tk.Button(root, text = 'Right', command=lambda t='Right':btn_clicked(t), height=2, width=10).place(x=230,y=452)

root.mainloop()

