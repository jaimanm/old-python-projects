# game where the user tries to make the shortest sentence using all the letters in the alphabet

# imports
from time import sleep
import enchant

# setup the enchant language detection module:
d = enchant.Dict("en_US")

# functions
def printString(string, pause=False): # function to print output in a cooler way
    for char in string:
        print(char, end="")
        sleep(0.03)
    if pause:
        sleep(2)
    print()
        
def getInput(): # function to get the user's guess
    printString("\nPlease enter your guess, or 'end' to quit:")
    return input()

def isPangram(guess): # function to check if the guess is a pangram
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guess_contains = ""
    for char in guess:
        if char in alphabet:
            guess_contains += char
    result = True
    for letter in alphabet:
        if letter not in guess_contains:
            result = False
            break
    return result

def validateInput(guess): # function to check if the guess is all english
    guess = guess.lower()
    guess = list(guess)
    for char in guess:
        if char == " " or char == "." or char == "," or char == "'" or char == "!" or char == "?": # remove all characters from the input
            position = guess.index(char)
            del guess[position] # remove all whitespace from the guess
    isValid = True
    for word in guess:
        if d.check(word) == False:
            isValid = False
            break
    return isValid, guess
    
def scores(guess, highScore): # function to calculate the score and update the high score
    score = len(guess)
    printString(f"Your score is: {score}\n")
    if highScore == 0:
        printString(f"Congratulations! You have guessed your first pangram! Keep trying to guess a shorter one!")
    elif score < highScore:
        printString(f"Congratulations! You have beaten your high score of: {highScore}", True)
        printString(f"Your new high score is: {score}")
    highScore = score
    return highScore

# intro
printString("Press enter to start.")
emptyInput = input()
if emptyInput != "skip intro":
    printString("Welcome To:")
    printString("------------------JAIMAN'S WORD GAME------------------\n", True)
    printString("Directions:\nYou must guess the shortest PANGRAM that you can. A PANGRAM  is a sentence that contains every letter of the alphabet.\n", True)
    printString("Good Luck!!")
    sleep(1)

# main game loop
highScore = 0
while True:
    guess = getInput()
    if guess.lower() == "end":
        break
    else:
        input_is_valid, guess = validateInput(guess)
        if input_is_valid:
            if isPangram(guess):
                highScore = scores(guess, highScore)
            else:
                printString("Your guess wasn't a pangram. Try again!", True)
        else:
            printString("Please enter a valid guess (hint: english words, no symbols like # and &, and no numbers).\n")
            sleep(2)
