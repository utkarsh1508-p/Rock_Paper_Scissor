from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()  # main window object
root.title('Rock Paper Scissor')  # Title of GUI window
root.geometry('800x680')  # Size of window

# Creating canvas
canvas = Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)

# Creating labels on GUI window
l1 = Label(root, text='Player', font=('Algerian', 25))
l2 = Label(root, text='Computer', font=('Algerian', 25))
l3 = Label(root, text='Vs', font=('Algerian', 40))

# Placing all the labels on window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

# Default image
img_p = Image.open("default.jpeg")  # Opening image
img_p = img_p.resize((300, 300))  # Resizing image
img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flipping image from left to right
# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

# Rock image
rock_p = Image.open('rock.jpeg')  # Opening image
rock_p = rock_p.resize((300, 300))  # Resizing image
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flipping image from left to right
# Loading images to put on canvas
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

# Paper image
paper_p = Image.open('paper.jpeg')  # Opening image
paper_p = paper_p.resize((300, 300))  # Resizing image
paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flipping image from left to right
# Loading images to put on canvas
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

# Scissor image
scissor_p = Image.open('scissor.jpeg')  # Opening image
scissor_p = scissor_p.resize((300, 300))  # Resizing image
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flipping image from left to right
# Loading images to put on canvas
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

# Selection image
img_s = Image.open("Selection.jpeg")  # Opening image
img_s = img_s.resize((300, 130))  # Resizing image
img_s = ImageTk.PhotoImage(img_s)  # Loading image to put on canvas

# Putting image on canvas on specific coordinates
canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)


# game function
def game(player):
    select = [1, 2, 3]
    computer = random.choice(select)  # Randomly selects option for computer

    # Setting image for player on canvas
    if player == 1:
        canvas.create_image(0, 100, anchor=NW, image=rock_p)  # Puts rock image on canvas
    elif player == 2:
        canvas.create_image(0, 100, anchor=NW, image=paper_p)  # Puts paper image on canvas
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_p)  # Puts scissor image on canvas

    # Setting image for computer on canvas
    if computer == 1:
        canvas.create_image(500, 100, anchor=NW, image=rock_c)  # Puts rock image on canvas
    elif computer == 2:
        canvas.create_image(500, 100, anchor=NW, image=paper_c)  # Puts paper image on canvas
    else:
        canvas.create_image(500, 100, anchor=NW, image=scissor_c)  # Puts scissor image on canvas

    # Obtaining result by comparison
    if player == computer:  # Case of DRAW
        res = 'Draw'
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):  # Case of player's win
        res = 'You won'
    else:  # Case of computer's win
        res = 'Computer won'

    # Putting result on canvas
    canvas.create_text(390, 600, text='Result:- ' + res, fill="black", font=('Algerian', 25), tag='result')


# Function for clear button
def clear():
    canvas.delete('result')  # Removes result from canvas

    # Puts default image on canvas
    canvas.create_image(0, 100, anchor=NW, image=img_p)
    canvas.create_image(500, 100, anchor=NW, image=img_c)


# Button for selecting rock
rock_b = Button(root, text='Rock', command=lambda: game(1))
rock_b.place(x=35, y=487)

# Button for selecting paper
paper_b = Button(root, text='Paper', command=lambda: game(2))
paper_b.place(x=128, y=487)

# Button for selecting scissor
scissor_b = Button(root, text='Scissor', command=lambda: game(3))
scissor_b.place(x=220, y=487)

# Button for clear
clear_b = Button(root, text='CLEAR', font=('Times', 10, 'bold'),  width=10, command=clear).place(x=370, y=28)

root.mainloop()
