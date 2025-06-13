"""
Program Name
Program description
Author: Arthur Belanger
Date created: 
Notes:Write a Python Program to check whether a given number is a palindrome
"""

import time
divider = ("_ _ _ ")
print(divider * 3)

def main():
    s = input("What is the wording you want to test for a palindrome? ")
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print("This is not a palindrome.")
    
if __name__ == '__main__':
    main()




print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    