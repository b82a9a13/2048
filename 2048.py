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

#Define start button and exit button, then place them
startbtn = tk.Button(root, text='Start Game', command=lambda:start_game(), height=2, width=10)
startbtn.place(x=(width/2)-40,y=(height/2))
exitbtn = tk.Button(root, text='Exit', command=lambda:exit_program(), height=2, width=10)
exitbtn.place(x=(width/2)-40, y=(height/2)+50)

#Define end game button
endbtn = tk.Button(root, text='End Game', command=lambda:end_game(), height=2, width=10)

#Define restart game button
restartbtn = tk.Button(root, text='Restart Game', command=lambda:restart_game(), height=2, width=10)

#Define game buttons
leftbtn = tk.Button(root, text='Left', height=2, width=10)
upbtn = tk.Button(root, text='Up', height=2, width=10)
downbtn = tk.Button(root, text='Down', height=2, width=10)
rightbtn = tk.Button(root, text='Right', height=2, width=10)

#Function is called to close the program
def exit_program():
    root.destroy()

#Function is called to start the game
def start_game():
    values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    startbtn.place_forget()
    exitbtn.place_forget()
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
            canvas.create_text(secheight/2, secwidth/2, text=values[y][xx], fill='black', font=('Arial 25 bold'))
        elif xx == 0:
            canvas.create_text(secheight/2, (secwidth*y)+(secwidth/2), text=values[y][xx], fill='black', font=('Arial 25 bold'))
        elif y == 0:
            canvas.create_text((secheight*xx)+(secheight/2), secwidth/2, text=values[y][xx], fill='black', font=('Arial 25 bold'))
        else:
            canvas.create_text((secheight*xx)+(secheight/2), (secwidth*y)+(secwidth/2), text=values[y][xx], fill='black', font=('Arial 25 bold'))
    canvas.pack()

    #Draw buttons and add a command for when the button is clicked
    endbtn.place(x=0, y=405)
    restartbtn.place(x=320, y=405)
    leftbtn.config(command=lambda t='Left':btn_clicked(t))
    leftbtn.place(x=70,y=452)
    upbtn.config(command=lambda t='Up':btn_clicked(t))
    upbtn.place(x=150,y=410)
    downbtn.config(command=lambda t='Down':btn_clicked(t))
    downbtn.place(x=150,y=452)
    rightbtn.config(command=lambda t='Right':btn_clicked(t))
    rightbtn.place(x=230,y=452)

    #Function disables buttons
    def disable_btns():
        leftbtn.config(state="disabled")
        upbtn.config(state="disabled")
        downbtn.config(state="disabled")
        rightbtn.config(state="disabled")

    #Function enables buttons
    def enable_btns():
        leftbtn.config(state="enabled")
        upbtn.config(state="enabled")
        downbtn.config(state="enabled")
        rightbtn.config(state="enabled")

    #Function returns True/False dependant if there are any empty spaces
    def empty_space():
        return any(any(value == 0 for value in row) for row in values)

    #Update canvas and add a new 2 in a empty square
    def update_canvas():
        global canvas
        #Check if there is a empty square
        contains_zero = empty_space()
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
                
    #Function is called to check whether the game has been won
    def game_won():
        return any(any(value == 2048 for value in row) for row in values)

    #Define function for when a button is clicked
    def btn_clicked(t):
        game_wo = game_won()
        if game_wo == True:
            messagebox.showinfo("Message","Game Won!")
        elif game_wo == False:
            disable_btns
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
            enable_btns

#Function is called to return to the menu
def end_game():
    canvas.pack_forget()
    canvas.delete('all')
    leftbtn.place_forget()
    rightbtn.place_forget()
    upbtn.place_forget()
    downbtn.place_forget()
    endbtn.place_forget()
    restartbtn.place_forget()
    startbtn.place(x=(width/2)-40,y=(height/2))
    exitbtn.place(x=(width/2)-40,y=(height/2)+50)

#Function is called to restart the game
def restart_game():
    canvas.pack_forget()
    canvas.delete('all')
    start_game()

root.mainloop()
