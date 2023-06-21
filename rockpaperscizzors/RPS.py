from tkinter import *
import random
# initialize window
root = Tk()
root.geometry('800x600')
root.resizable(0,0) #allow window reside
root.title('Rock,Paper,Scissors Game')
root.config(bg ='silver')
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 18 bold', bg = 'orange').pack()

user_choice = StringVar()
Label(root, text = 'Please enter your choice: rock, paper or scissors' , font='arial 12 bold', bg = 'seashell2').place(x = 210,y=70)
Entry(root, font = 'arial 15', textvariable = user_choice , bg = 'lightblue').place(x=290 , y = 130) #Create an input text field
Result = StringVar()

def gameStart():
    comp_choice = random.choice([1, 2, 3])
    if comp_choice == 1:
        comp_choice = 'rock'
    elif comp_choice ==2:
        comp_choice = 'paper'
    else:
        comp_choice = 'scissors'
    user_pick = user_choice.get()
    if user_pick == comp_choice:
        Result.set('It is a tie!')
    elif user_pick == 'rock' and comp_choice == 'paper':
        Result.set('Too bad, you lost, computer picked ' + comp_choice)
    elif user_pick == 'rock' and comp_choice == 'scissors':
        Result.set('Congrat, you win, computer picked ' + comp_choice)
    elif user_pick == 'paper' and comp_choice == 'scissors':
        Result.set('Better luck next time, computer picked ' + comp_choice)
    elif user_pick == 'paper' and comp_choice == 'rock':
        Result.set('Nice, a win for you, computer picked ' + comp_choice)
    elif user_pick == 'scissors' and comp_choice == 'rock':
        Result.set('Oh dear, a lost for you, computer picked ' + comp_choice)
    elif user_pick == 'scissors' and comp_choice == 'paper':
        Result.set('You beat the computer, it picked ' + comp_choice)
    else:
        Result.set('Invalid input, please only choose: rock, paper or scissors')

def resetGame():
    Result.set("") 
    user_choice.set("")
    
def exitGame():
    root.destroy() #stop the main loop to quit the game

Entry(root, font = 'arial 9 bold', textvariable = Result, bg ='green',width = 50,).place(x=220, y = 250)
Button(root, font = 'arial 12 bold', text = 'Start'  ,padx =5,bg ='yellow' ,command = gameStart).place(x=370,y=190)
Button(root, font = 'arial 12 bold', text = 'Reset'  ,padx =5,bg ='red' ,command = resetGame).place(x=250,y=310)
Button(root, font = 'arial 12 bold', text = 'Quit'  ,padx =5,bg ='blue' ,command = exitGame).place(x=480,y=310)
root.mainloop() #a method on the main window which we execute when we want to run our application. 
#This method will loop forever, until user exit the program