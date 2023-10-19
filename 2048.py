#Import tkinter which is used to create a GUI app
import tkinter as tk
from random import randint
from tkinter import messagebox
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk

#Define required variables
root = tk.Tk()
height = 400
width = 400
secheight = 400/4
secwidth = 400/4
values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Set the application title, size and disable resizing
root.title("2048")
root.geometry(f"{width}x500")
root.resizable(False,False)

#Define the canvas varaiable
canvas = tk.Canvas(root, width=width, height=height, bg="lightgrey")

#Define start button, exit button and upload button, then place them
startbtn = tk.Button(root, text='Start Game', command=lambda:start_game(), height=2, width=11)
startbtn.place(x=(width/2)-40,y=(height/2))
uploadbtn = tk.Button(root, text='Upload Images', command=lambda:upload_images(), height=2, width=11)
uploadbtn.place(x=(width/2)-40, y=(height/2)+50)
exitbtn = tk.Button(root, text='Exit', command=lambda:exit_program(), height=2, width=11)
exitbtn.place(x=(width/2)-40, y=(height/2)+100)

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

def exit_menu():
    startbtn.place_forget()
    exitbtn.place_forget()
    uploadbtn.place_forget()

#Function is called to start the game
def start_game():
    values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    exit_menu()
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
    create_menu()

#Function is called to create the main menu
def create_menu():
    startbtn.place(x=(width/2)-40,y=(height/2))
    uploadbtn.place(x=(width/2)-40,y=(height/2)+50)
    exitbtn.place(x=(width/2)-40,y=(height/2)+100)
    
#Function is called to restart the game
def restart_game():
    canvas.pack_forget()
    canvas.delete('all')
    start_game()


#Create Upload Buttons
uploadText = Label(root, text='Select a image for each number')
#Define array of upload buttons
imageBtns = [
    [
        tk.Button(root, text='2', command=lambda:open_image(0)),
        tk.Button(root, text='4', command=lambda:open_image(1)),
        tk.Button(root, text='8', command=lambda:open_image(2)),
        tk.Button(root, text='16', command=lambda:open_image(3))
    ],[
        tk.Button(root, text='32', command=lambda:open_image(4)),
        tk.Button(root, text='64', command=lambda:open_image(5)),
        tk.Button(root, text='128', command=lambda:open_image(6)),
        tk.Button(root, text='256', command=lambda:open_image(7))
    ],[
        tk.Button(root, text='512', command=lambda:open_image(8)),
        tk.Button(root, text='1028', command=lambda:open_image(9)),
        tk.Button(root, text='2048', command=lambda:open_image(10))
    ]
]
#Array used to store the images
img = [None, None, None, None, None, None, None, None, None, None, None]
#Array used to store the labels
labels = [None, None, None, None, None, None, None, None, None, None, None]
#Submit button
subBtn = tk.Button(root, text='Submit Images', command=lambda:submit_images())
#.place(x=350, y=450)
subError = Label(root, text='You are missing image(s) for numbered value(s)', fg='red')
#Error text
panel = Label(root, text='Invalid Image size, it must be 100px by 100px', fg='red')
#Back button
backBtn = tk.Button(root, text='Go Back', command=lambda:upload_back())
#Function is called when the back button is clicked
def upload_back():
    uploadText.pack_forget()
    for x in imageBtns:
        for y in x:
            y.place_forget()
    subBtn.place_forget()
    backBtn.place_forget()
    for x in labels:
        if x != None:
            x.place_forget()
    del_img_error()
    create_menu()
#Function is called to open the upload images section

def upload_images():
    #Remvoe menu buttons
    exit_menu()
    #Title
    uploadText.pack(side="top")
    xp = 0;
    #Place upload image buttons
    for x in imageBtns:
        yp = 0
        for y in x:
            if xp == 0:
                y.place(x=155+(20*yp),y=75)
            elif xp == 1:
                if yp > 2:
                    y.place(x=142+(27*yp),y=105)
                else:
                    y.place(x=142+(25*yp),y=105)
            elif xp == 2:
                if yp > 1:
                    y.place(x=146+(33*yp),y=135)
                else:
                    y.place(x=146+(30*yp),y=135)
            yp += 1
        xp += 1
    #Add back and submit buttons
    subBtn.place(x=305, y=135)
    backBtn.place(x=5, y=135)

#Function is called to remove image error messages
def del_img_error():
    #forget error pack if it exists
    subError.pack_forget()
    panel.pack_forget()
def open_image(pos):
    #Need to include a global varaible to store the img
    global img
    del_img_error()
    #get fjle and define the allowed file types
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if filePath:
        with open(filePath, "rb") as image_file:
            #Create a variable with the image
            im = Image.open(filePath)
            #Check the size of the image is 100x100
            width, height = im.size
            if width != 100 and height != 100:
                #Output error message
                panel.pack(side="top")
            else:
                #Define the x and y position dependant on the position provided
                xPos = 0
                yPos = 175
                if pos > 0:
                    if pos >= 8 or pos >= 4:
                        if pos >= 8:
                            xPos += 100*((pos-4)%4)+50
                        elif pos >= 4:
                            xPos += 100*(pos%4)   
                        yPos += 102*(pos//4)
                    else:
                        xPos += 100*pos
                #Create a image variable within an array
                img[pos] = ImageTk.PhotoImage(im)
                #Forget the old pack if it exists
                if labels[pos] != None:
                    labels[pos].pack_forget()
                #Add the image to a label and pack to the UI
                labels[pos] = Label(root, image=img[pos])
                labels[pos].place(x=xPos, y=yPos)

def submit_images():
    del_img_error()
    if any(value == None for value in img) == True:
        subError.pack(side='top')
    else:
        upload_back()

root.mainloop()
