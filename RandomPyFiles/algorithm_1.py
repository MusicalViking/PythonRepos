"""
Program Name : Algorithm #1 from GPT 
Program description
Author: Arthur Belanger
Date created: 
Notes: Skills practiced:
Dictionaries, string iteration, understanding frequency maps.

Problem Description : Write a function that returns the first 
character in a string that does not repeat. If all characters 
repeat, return None


Problem Solution

"""
from collections import Counter
import time

divider = ("_ _ _ ")
print(divider * 3)

def main(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

example = input("Type in your string to find first none repeating character: \n")
result = main(example)
print(result)

print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    