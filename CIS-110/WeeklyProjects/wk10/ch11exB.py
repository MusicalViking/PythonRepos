"""
Program Name : ch11exB
Program description : In class exercise for random number
Author: Arthur Belanger
Date created: 4-11-25
Notes: Generates random number using seed

"""
import time
from random import random, seed

divider = ("_ _ _ ")
print(divider * 3)

def main():
    seed(123456)
    printIntro()
    n = getInputs()
    printNumbers(n)

def printIntro():
    print("Hello, welcome! Now let's generate some random numbers")

def getInputs():
    return int(input("How many random numbers do you want printed today? "))

def printNumbers(n):
    for _ in range(n):
        print(random())

if __name__ == "__main__":
    main()


print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program #ch11exB ")
print(time.ctime())
    
