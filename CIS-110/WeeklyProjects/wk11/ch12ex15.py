"""
Program Name : ch12ex15
Program description : pulls random cards showing names and rank
Author: Arthur Belanger
Date created: 4-23-25
Notes:
"""
import time
from random import randrange
divider = ("_ _ _ ")
print(divider * 3)

class Card():
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self.__suit

    def value(self):
        if self.getRank() < 10:
            return self._rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        if self._suit =='d':
            suitStr = "Diamonds"
        elif self._suit == 'c':
            suitStr = "Clubs"
        elif self._suit == 's':
            suitStr = "Spades"
        elif self._suit == 'h':
            suitStr = "Hearts"
        return f'{ranks[self._rank]} of {suitStr}'
    
def main():
    print("Test card classes")
    n = int(input("How many cards would you like to see? "))
    for i in range(n):
        rank = randrange(1, 14)
        suit = "dchs"[randrange(4)]
        randCard = Card(rank, suit)
        print(f'Card {randCard} has value: {randCard.value()}')

if __name__ == '__main__':
    main()

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program #ch12ex15 ")
print(time.ctime())
    