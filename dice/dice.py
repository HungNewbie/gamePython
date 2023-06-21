import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('800x600')
root.title('Dice rolling')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack() #pack method to arrange widgets in row and column form.
# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Welcome to my game!",
   fg = "light green",
     bg = "dark orange",
     font = "Helvetica 15 bold italic")
HeadingLabel.pack()
# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']
# randomly choose a number and a png picture between
# 1 to 6 
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# Image label
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
# pack a widget
ImageLabel.pack( expand=True)

# fucntion for button 'Dice Roll'
def diceRoll():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # image change according to the random number
    ImageLabel.configure(image=DiceImage)
    # Reference
    ImageLabel.image = DiceImage
# Create button "Dice Roll". It will use the function diceRoll()
rollButton = tkinter.Button(root, text='Dice Roll', fg='red', command=diceRoll)
# pack a widget in the parent widget
rollButton.pack( expand=True)
# call the tkinter loop to keep the window open
root.mainloop()