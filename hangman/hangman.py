import random
import time # add delay

name = input("Enter your name: ")
print("Hello " + name + "!")
time.sleep(2)
print("It's time to start the game!")
time.sleep(3)

def game():
    global count
    global display
    global word
    global already_guessed
    global wordLength
    global playAgain
    words_list = ["balance","darkness","enemy","funny","harsh","jackal","lumber","master","physical","railway","silence", "tower", "village", "xilam", "zombie"]
    word = random.choice(words_list)
    wordLength = len(word)
    count = 0
    display = '_' * wordLength
    already_guessed = []
    playAgain = ""

    # the game will be executed again by using a loop after the first round ends:
def anotherGame():
    global playAgain
    playAgain = input("Do You want to play again? y or n? \n")
    while playAgain not in ["y","n","Y","N"]:
        playAgain = input("Wrong input, please only use either y, n, Y or N \n")
    if playAgain == "y" or "Y":
        game()
        hangman()
    elif playAgain == "n" or "N":
        print("We hope to see you again soon!")
        exit()

        # check if the user input is correct or not. And limit the maximum number of guess to 5. Strip method to 
        # remove any space in user input. Extend method is adding the correct guess to the word.
def hangman():
    global count
    global display
    global word
    global already_guessed
    global playAgain
    limit = 5
    letter = input("A new hangman word for you: " + display + " Please enter a letter: \n")
    letter = letter.strip()
    if len(letter.strip()) == 0 or len(letter.strip()) >= 2 or letter <= "9":
        print("Please enter a letter only\n")
        hangman()
    elif letter in word:
        already_guessed.extend([letter])
        index = word.find(letter)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + letter + display[index + 1:]
        print(display + "\n")
    elif letter in already_guessed:
        print("You've already guessed this letter, try another one.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("You guessed a wrong letter. " + str(limit - count) + " guesses remaining.\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("You guessed a wrong letter again. " + str(limit - count) + " guesses remaining.\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Another wrong letter. Warning, you only have " + str(limit - count) + " guesses left.\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("This is your final chance. " + str(limit - count) + " more wrong letter and you are out! \n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Oh dear, you got a hangman. Game over!\n")
            print("The correct word is:",already_guessed,word)
            anotherGame()
    if word == '_' * wordLength:
        print("Good job, you found the correct word!")
        anotherGame()
    elif count != limit:
        hangman()
game()
hangman()