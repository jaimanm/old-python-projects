from time import sleep
from secrets import choice

# game loop:
# print current board
# generate random word
# print blank spaces
# print list of wrong letters
# get user guess
# check if guess is in the word and where
#   if right - update blanks
#   if wrong - update # of mistakes
# end loop


def printCool(string, pause=False):
    for char in string:
        print(char, end='')
        sleep(0.1)
    print()
    if pause:
        sleep(1)

def drawBoard(mistakes, blanks, wrong_guesses):
    top_row = '  ---|'
    head_board = ['     |', ' ()  |']
    body_board = ['     |', ' ||  |' , '/||  |', '/||\ |']
    legs_board = ['     |', ' /   |', ' /\  |']
    bottom_row = '  ___|__'
    
    print(top_row)
    # print head section
    if mistakes >= 1:
        print(head_board[1])
    else:
        print(head_board[0])
    # print body section
    if mistakes >= 2 and mistakes < 5:
        print(body_board[mistakes-1])
    elif mistakes >= 5:
        print(body_board[3])
    else:
        print(body_board[0])
    # print legs section
    if mistakes >= 5:
        print(legs_board[mistakes-4])
    else:
        print(legs_board[0])
        
    print(bottom_row)
    print()
    for char in blanks:
        print(char, end=' ')
    print('\n')
    print('Letters guessed wrong:')
    for letter in wrong_guesses:
        print(letter, ' ', end='')
    

## drawBoard() code is a condensed version of the following:
##    print(top_row)
##    if mistakes == 0:
##        print(head_board[0])
##        print(body_board[0])
##        print(legs_board[0])
##    elif mistakes == 1:
##        print(head_board[1])
##        print(body_board[0])
##        print(legs_board[0])
##    elif mistakes == 2:
##        print(head_board[1])
##        print(body_board[1])
##        print(legs_board[0])
##    elif mistakes == 3:
##        print(head_board[1])
##        print(body_board[2])
##        print(legs_board[0])
##    elif mistakes == 4:
##        print(head_board[1])
##        print(body_board[3])
##        print(legs_board[0])
##    elif mistakes == 5:
##        print(head_board[1])
##        print(body_board[3])
##        print(legs_board[1])
##    elif mistakes == 6:
##        print(head_board[1])
##        print(body_board[3])
##        print(legs_board[2])
##    print(bottom_row)

def getGuess():
    while True:
        printCool('Enter your guess:')
        guess = input()
        if guess.isalpha() and len(guess) == 1:
            return guess.lower()
            break
        else:
            printCool('Please enter a letter.')

def checkGuess(guess, word, blanks, mistakes):
    if guess in word:
        # update blanks
    else:
        mistakes += 1
    return blanks, mistakes

mistakes = 6
blanks = ['_', 'o', 'o', '_']
wrong_guesses = 'abdef'
print(getGuess())
drawBoard(mistakes, blanks, wrong_guesses)
