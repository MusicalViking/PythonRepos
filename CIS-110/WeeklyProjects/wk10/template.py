"""
Program Name : Program #7
Program description : simulates a blackjack game
Author: Arthur Belanger
Date created: 4-14-25
Notes: I added in a if statement to get the ace factor from 1 to 11 and back if it is over 21, it plays like a actual blackjack game.
I was also playing with the intro and made it a bit better....I am going to make a gui for this later on.
"""

import time
import random
import sys

divider = ("_ _ _ _ _  ")
print(divider * 5)

def main():
    printIntro()
    n = getInputs()
    totalWins = startGame(n)
    printResults(totalWins, n)

def printIntro():
    intro = input("Are you ready to try your luck at blackjack? (yes/no): ").strip().lower()
    if intro in ['yes', 'y']:
        print("Great! Hope you brought some $$$.\n")
    else:
        print("Maybe you should go to gamblers anonymous! Goodbye.")
        sys.exit()

def getInputs():
    return int(input("How many games are we playing? "))

def startGame(n):
    wins = 0
    for _ in range(n):
        if playGame() == 1:
            wins += 1
    return wins

def playGame():
    playerHand = dealHand()
    dealerHand = dealHand()

    print(f"\n{divider} New Game {divider}")
    print(f"Your starting hand: {playerHand} (Score: {addScore(playerHand)})")
    print(f"Dealer's face-up card: [{dealerHand[0]}, ?]")

    playerScore, playerHand = playerTurn(playerHand)
    if playerScore > 21:
        print("You busted! Dealer wins.")
        return 0

    dealerScore, dealerHand = dealerTurn(dealerHand)
    return chooseWinner(playerScore, dealerScore)

def dealHand():
    return [dealCard(), dealCard()]

def dealCard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   
    if cards == 1 and addScore < 10:
        cards = 11
    return random.choice(cards)

def addScore(hand):
    score = sum(hand)
    aces = hand.count(1)
    while aces > 0 and score + 10 <= 21:
        score += 10
        aces -= 1
    return score

def playerTurn(hand):
    while True:
        score = addScore(hand)
        if score > 21:
            return score, hand
        action = input("Do you want to 'hit' or 'stay'? ").lower()
        if action == 'hit' or action == 'h':
            hand.append(dealCard())
            print(f"Your hand: {hand} (Score: {addScore(hand)})")
        elif action == 'stay' or action == 's':
            break
    return addScore(hand), hand

def dealerTurn(hand):
    print(f"\nDealer's turn. Starting hand: {hand} (Score: {addScore(hand)})")
    while addScore(hand) < 17:
        print("Dealer hits.")
        hand.append(dealCard())
        print(f"Dealer's hand: {hand} (Score: {addScore(hand)})")
    return addScore(hand), hand

def chooseWinner(playerScore, dealerScore):
    if dealerScore > 21 or playerScore > dealerScore:
        print("You win!")
        return 1
    elif playerScore < dealerScore:
        print("Dealer wins!")
        return 0
    else:
        print("It's a push (tie)!")
        return 0

def printResults(wins, totalGames):
    print(f"\nGames played: {totalGames}")
    print(f"Games won: {wins}")
    print(f"Win rate: {wins / totalGames:.1%}")

if __name__ == "__main__":
    main()

print(divider * 5)
print("Arthur Belanger")
print("CIS-110 - Assignment #7 ")
print(time.ctime())
    

