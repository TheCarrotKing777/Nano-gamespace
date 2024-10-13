import random
import sys

def startgame():
    number = random.randint(1, 20)
    guess = 0
    while guess != number:
        guess = int(input("------------------------------------------------------------------\nRaad een nummer tussen de 1 en 20\n------------------------------------------------------------------\n"))
        if guess < number:
            print("Raad hoger!")
        elif guess > number:
            print("Raad lager!")
        else:
            print("------------------------------------------------------------------\nCorrect! Goed gedaan\n------------------------------------------------------------------")


sys.modules[__name__] = startgame 