# PicoFermiBagel
#
# A puzzle game where the user must guess a number
# based on the given clues
#

import random

# game setting constants
NUM_OF_DIGITS = 3 # number of digits the hidden number will have
MAX_GUESSES = 10 # number of times the user has to guess the number


def main():
    # Introduction
    print('PicoFermiBagels')
    print('There is a hidden {}-digit number with no repeating digits.'.format(NUM_OF_DIGITS))
    print('Try to guess what it is, you will have {} tries to guess it.'.format(MAX_GUESSES))
    print('''Here are some clues:
What is Said:       What it means:
Pico                One of the digits is correct, but in the wrong position
Fermi               One digit is correct and in the right position
Bagel               No digit is correct
        
For example, if the secret number was 123 and your guess was 135, the 
response would be Fermi Pico.''')





    while True: # Main Game Loop
        secretNum = getSecretNum()
        print('The hidden number has been set.')
        print('The hidden number has {} digits and you have {} tries to guess it'.format(NUM_OF_DIGITS, MAX_GUESSES))

        numOfGuesses = 1
        while numOfGuesses <= MAX_GUESSES: # runs until past maximum allowed guesses

            userGuess = ''
            # checks user input is the right length and is a number
            while len(userGuess) != NUM_OF_DIGITS or not userGuess.isdigit():
                userGuess = input('Enter in your guess: >')

            response = checkNum(guess=userGuess, secretNum=secretNum)
            print(response)
            numOfGuesses += 1


            if userGuess == secretNum:  # user guessed the hidden number
                break
            if numOfGuesses > MAX_GUESSES:
                print('Sorry, you ran out of guesses. :( ')
                print('The hidden number was {}'.format(secretNum))

        # Asks the user if they want to play again
        print('Do you want to play again? (Enter y to play again)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing. Goodbye.')

# Checks each digit of the user's guess input and the hidden number.
# Return a string of hints based on how many numbers in the user's
# input are in the hidden number as well as their placements.
def checkNum(guess: str, secretNum: str) -> str:
    response = []

    if guess == secretNum:      # response for the guess being the hidden number
        return 'Congratulations, you got the number!'

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            response.append('Fermi')     # correct number and correct position
        elif guess[i] in secretNum:
            response.append('Pico')      # correct number but wrong position

    if len(response) == 0:
        return 'Bagel'  # returns Bagel if there were no matches
    else:
        random.shuffle(response)    # randomizes the position of the hints to prevent cheating
        return ' '.join(response)


# Generates a new hidden number with the digit length base on NUM_OF_DIGITS
def getSecretNum() -> int:
    nums = list('0123456789')   # creates a list of all numbers (prevents repeating numbers)
    random.shuffle(nums)    # randomizes the position of the numbers

    secretNum = ''
    for i in range(NUM_OF_DIGITS):  # Adds numbers according to the number of digits
        secretNum += str(nums[i])

    return secretNum

if __name__ == '__main__':
    main()
