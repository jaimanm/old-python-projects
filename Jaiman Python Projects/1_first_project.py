# this is my first project in python!!! :)

#imports
from time import sleep

# functions
def printString(string):
    for char in string:
        print(char, end="")
        sleep(0.08)

def getName(): # get the name of the user
    printString("What is your name?\n")
    name = input()
    return name

def identify(name): # interpret the name taken from getName, print a response accordingly
    checkName = name.lower()
    if checkName == "jaiman": # check for the creator of the project (me!)
        printString("Welcome, Creator of this Project!")
        return True
    else:
        hasDigit = False
        for char in name: # check if the input given has any numbers in it
            if char.isdigit():
                hasDigit = True
                break
        if hasDigit:
            printString("Are you sure that's a real name?\n") # prompt the user to try again
            return False
        else:
            printString(f"Nice to meet you, {name}!") # greet the unknown user
            return True 

# main loop
printString("Hello there! ")
while True:
    userName = getName()
    endProgram = identify(userName)
    if endProgram:
        break