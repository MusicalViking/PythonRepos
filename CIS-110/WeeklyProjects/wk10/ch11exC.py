"""
Program Name : ch11exC
Program description : Shows how numbers are uniformly distributed.
Author: Arthur Belanger
Date created: 4-12-25
Notes:

"""
import time
from random import randrange, seed
divider = ("_ _ _ ")
print(divider * 3)

def main():
    seed(1234546)
    printIntro()
    n = getInputs()
    results = generateSamples(n)
    printSummary(n, results)

def printIntro():
    print("This program confirms PRN are uniformly distrubuted")

def getInputs():
    return int(input("How many samples sholld I take?"))

def generateSamples(n):
    results = [0,0,0,0,0,0]
    for i in range(n):
        sample = randrange(0,6)
        results[sample] = results[sample] + 1
    return results

def printSummary(n, results):
    for i in range(0,6):
        print(f"{i}: {results[i]/n:6.2%}")

if __name__ == '__main__' : 
    main()


print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - ch11exC ")
print(time.ctime())
    
