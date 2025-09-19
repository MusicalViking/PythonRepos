"""
Program Name : Program #7
Program description : simulates a blackjack game
Author: Arthur Belanger
Date created: 4-14-25
Notes: I wrote an entire program out that had a whole real game going and liked it... then I reread the 
directions in brightspace and had to change it up but I am saving that version for a customTkinter GUI.
I did add a couple little things like a sys.exit and a input("\nClick Enter or close the window to exit...")
to keep it open when it runs off the terminal.
"""
import time
import random
import sys

divider = ("_ _ ")
print(divider * 5)

def main():
    printIntro()
    numGames = getGames()
    standValue = getStandValue()
    totalWins = startGame(numGames, standValue)
    printResults(totalWins, numGames, standValue)


def printIntro():
    intro = input("Are you ready to try your luck at blackjack? (yes/no): ").strip().lower()
    if intro in ['yes', 'y']:
        print("Great! Hope you brought some $$$.\n")
    else:
        print("Maybe you should go to gamblers anonymous! Goodbye.")
        sys.exit()

def getGames():
    return int(input("How many games should be played? "))

def getStandValue():
    return int(input("What stand value do you want? "))

def simNGames(numGames, targetScore):
    wins = 0
    for _ in range(numGames):
        if playGame(targetScore) == 1:
            wins += 1
    return wins

def startGame(numGames, standValue):
    wins = 0
    for _ in range(numGames):
        if playGame(standValue) == 1:
            wins += 1
    return wins

def playGame(targetScore):
    playerHand = dealFirstHand()
    dealerHand = dealFirstHand()
    playerScore, playerHand = playerTurn(playerHand, targetScore)
    if playerScore > 21:
        return 0
    dealerScore, dealerHand = dealerTurn(dealerHand, playerScore)
    return determineWinner(playerScore, playerHand, dealerScore, dealerHand)

def dealFirstHand():
    return [dealCard(), dealCard()]

def playerTurn(hand, targetScore):
    while True:
        score = calculateScore(hand)
        if score > 21:
            return score, hand
        if score < targetScore:
            hand.append(dealCard())
        else:
            break
    return calculateScore(hand), hand

def dealerTurn(hand, playerScore):

    while calculateScore(hand) < 17:
        hand.append(dealCard())
        if calculateScore(hand) > 21:
            return calculateScore(hand), hand
    return calculateScore(hand), hand

def determineWinner(playerScore, playerHand, dealerScore, dealerHand):
    if dealerScore > 21:
        return 1
    elif playerScore > dealerScore:
        return 1
    elif playerScore < dealerScore:
        return 0
    else:
        return 0

def dealCard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   
    return random.choice(cards)

def calculateScore(hand):
    score = sum(hand)
    aces = hand.count(1)
    while aces > 0 and score + 10 <= 21:
        score += 10
        aces -= 1
    return score

def printResults(wins, numGames, standValue):
    print(f"\nGames played: {numGames}")
    print(f"Games won: {wins}")
    print(f"Win rate: {wins / numGames:.1%}")
    print(f"Player stand value {standValue}: Player wins {wins} out of {numGames} games")

if __name__ == "__main__":
    main()

print(divider * 5)
print("Arthur Belanger")
print("CIS-110 - Program #7 ")
print(time.ctime())
input("\nClick Enter or close the window to exit...")
    