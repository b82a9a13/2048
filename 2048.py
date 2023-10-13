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
def draw_canvas(canvas):
    #Draw verticle lines and horizontal lines
    fill = "black"
    for x in range(4):
        canvas.create_line(secwidth*x, height, secwidth*x, 0, fill=fill)
        canvas.create_line(0, secheight*x, width, secheight*x, fill=fill)
draw_canvas(canvas)

#Draw starting numbers 
for x in range(3):
    y = randint(0,3)
    xx = randint(0,3)
    while values[y][xx] == 2:
        y = randint(0,3)
        xx = randint(0,3)
    values[y][xx] = 2
    if xx == 0 and y == 0:
        canvas.create_text(secheight/2, secwidth/2, text='2', fill='black', font=('Arial 50 bold'))
    elif xx == 0:
        canvas.create_text(secheight/2, (secwidth*y)+(secwidth/2), text='2', fill='black', font=('Arial 50 bold'))
    elif y == 0:
        canvas.create_text((secheight*xx)+(secheight/2), secwidth/2, text='2', fill='black', font=('Arial 50 bold'))
    else:
        canvas.create_text((secheight*xx)+(secheight/2), (secwidth*y)+(secwidth/2), text='2', fill='black', font=('Arial 50 bold'))
canvas.pack()

#Update canvas and add a new 2 in a empty square
def update_canvas(canvas):
    #Check if there is a empty square
    contains_zero = any(any(value == 0 for value in row) for row in values)
    if contains_zero == False:
        messagebox.showinfo("Message","Game Over!")
    elif contains_zero == True:
        #Remove all canvas elements
        for widget in root.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()
        #Create a new canvas
        canvas = tk.Canvas(root, width=width, height=height, bg="lightgrey")
        #Draw the grid
        draw_canvas(canvas)        
        #Add a new 2 to the values array
        yy = randint(0,3)
        xx = randint(0,3)
        while values[yy][xx] != 0:
            y = randint(0,3)
            xx = randint(0,3)
        values[yy][xx] = 2
        #Draw the values
        for y in range(len(values)):
            for x in range(len(values[y])):
                current = values[y][x] if values[y][x] != 0 else ''
                if x == 0 and y == 0:
                    canvas.create_text(secheight/2, secwidth/2, text=current, fill='black', font=('Arial 50 bold'))
                elif x == 0:
                    canvas.create_text(secheight/2, (secwidth*y)+(secwidth/2), text=current, fill='black', font=('Arial 50 bold'))
                elif y == 0:
                    canvas.create_text((secheight*x)+(secheight/2), secwidth/2, text=current, fill='black', font=('Arial 50 bold'))
                else:
                    canvas.create_text((secheight*x)+(secheight/2), (secwidth*y)+(secwidth/2), text=current, fill='black', font=('Arial 50 bold'))
        #Output the canvas
        canvas.pack()
            

#Define function for when a button is clicked
def btn_clicked(t, canvas):
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
            if t == 'Right' or t == 'Left':
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
                row.append(0)
                row.append(0)
                row.append(0)
            elif len(row) == 2:
                row.append(0)
                row.append(0)
            elif len(row) == 3:
                row.append(0)
            #Add row values back to values array
            if t == 'Left':
                values[y] = row
            elif t == 'Up':
                values[0][y] = row[0]
                values[1][y] = row[1]
                values[2][y] = row[2]
                values[3][y] = row[3]
            elif t == 'Down':
                values[3][y] = row[0]
                values[2][y] = row[1]
                values[1][y] = row[2]
                values[0][y] = row[3]
            elif t == 'Right':
                values[y][3] = row[0]
                values[y][2] = row[1]
                values[y][1] = row[2]
                values[y][0] = row[3]
        #Update canvas        
        update_canvas(canvas)

#Draw buttons
t = 'Left'
btn = tk.Button(root, text = 'Left', command=lambda t='Left', canvas=canvas:btn_clicked(t, canvas), height=2, width=10).place(x=70,y=452)
btn = tk.Button(root, text = 'Up', command=lambda t='Up', canvas=canvas:btn_clicked(t, canvas), height=2, width=10).place(x=150,y=410)
btn = tk.Button(root, text = 'Down', command=lambda t='Down', canvas=canvas:btn_clicked(t, canvas), height=2, width=10).place(x=150,y=452)
btn = tk.Button(root, text = 'Right', command=lambda t='Right', canvas=canvas:btn_clicked(t, canvas), height=2, width=10).place(x=230,y=452)

root.mainloop()


