import random
import sys


def ShowBoard():
   
    global word
    global guessed
    global stage
    global lives
    stages = [rf'''    +---+
    |   |
        |        Word: [ {' '.join(blankList)} ]
        |     Guessed: [ {', '.join(guessed)} ]
        |       Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
        |    Guessed: [ {', '.join(guessed)} ]
        |      Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
    |   |    Guessed: [ {', '.join(guessed)} ]
        |      Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
   /|   |    Guessed: [ {', '.join(guessed)} ]
        |      Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
   /|\  |    Guessed: [ {', '.join(guessed)} ]
        |      Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
   /|\  |    Guessed: [ {', '.join(guessed)} ]
   /    |      Lives: {lives}
        |
  =========''', rf'''    +---+
    |   |
    O   |       Word: [ {' '.join(blankList)} ]
   /|\  |    Guessed: [ {', '.join(guessed)} ]
   / \  |      Lives: {lives}
        |
  =========''']

    print('---------------------------------------------------------------')
    print(stages[stage])
    print('---------------------------------------------------------------')

def RevealLetters(input_letter):
    global lettersGood
    for i in range(len(chosen_word)):
        if chosen_word[i] == input_letter:
            blankList[i] = chosen_word[i]
            lettersGood += 1


lives = 6
stage = 0
lettersGood = 0
guessed = []

lijst = open('message.txt', 'r')
word_list = lijst.read()
lijst.close()
words = word_list.split('\n')


chosen_word = random.choice(words)

lettersNeeded = len(chosen_word)

blankList = list('_'*len(chosen_word))

def startgame():
    while True:
        ShowBoard()
        input_letter = input("Guess a letter!\n")
        
        if input_letter not in guessed:
            guessed.append(input_letter)

        if input_letter in chosen_word:
            RevealLetters(input_letter)

        else:
            lives -= 1
            stage += 1

        if lives == 0:
            ShowBoard()
            print("You Lost")
            break
        
        if lettersNeeded == lettersGood:
            ShowBoard()
            print("You Won")
            break

sys.modules[__name__] = startgame