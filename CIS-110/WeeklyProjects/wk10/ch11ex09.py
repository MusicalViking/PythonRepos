"""
Program Name : ch11ex09
Program description : Craps game
Author: Arthur Belanger
Date created: 4-13-25
Notes: I am going to play with customTkinter to make a gui and show each roll and win.
"""
import time
from random import randrange
divider = ("_ _ _ ")
print(divider * 3)

def main():
    printIntro()
    n = getInputs()
    wins = simNGames(n)
    printResults(wins, n)

def printIntro():
    print(" Want to know the chance of winning at craps?")

def getInputs():
    return int(input("How many games should we play? "))

def simNGames(n):
    wins = 0
    for _ in range(n):
        if winCraps():
            wins += 1
    return wins

def winCraps():
    roll = rollDice()
    if roll == 2 or roll == 3 or roll == 12:
        return False
    elif roll == 7 or roll == 11:
        return True
    else:
        point = roll
        return rollForPoint(point)

def rollForPoint(point):
    while True:
        roll = rollDice()
        if roll == point:
            return True
        elif roll == 7:
            return False

def rollDice():
    return randrange(1, 7) + randrange(1, 7)

def printResults(wins, n):
    print(f"\nWith {n} played games:")
    print(f"I won {wins} games.")
    print(f"The chance of winning is {wins/n:.1%}")

if __name__ == '__main__':
    main()

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - ch11ex09 ")
print(time.ctime())
    
