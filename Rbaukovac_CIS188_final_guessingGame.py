# Randy Baukovac, final Hangman/guessing game

# import .random to pick from set array
import random

# ask user for name, store user name is var "name"
name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ", name)
# generate a random array with a list of words
words = ['silly', 'computer', 'programmer', 'lights',
         'flag', 'brother', 'america', 'military',
         'life', 'water', 'game', 'see']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12

while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end="")

        else:
            print("_")
            # print(char, end="")

            # for every failure 1 will be added
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong letter then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character:")

    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character does not match the word
        # then “Wrong” will be given as output
        print("Wrong, guess again")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
