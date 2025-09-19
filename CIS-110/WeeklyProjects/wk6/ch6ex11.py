"""
Program Name : ch6ex11
Program description: In class exercises
Author: Arthur Belanger
Date created: 3-6-25
Notes:
"""
print("--------------------------------")
import time

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    try:
        year = int(input("What's the year: "))
        if isLeapYear(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid Input")

main()
print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - In class exercises ")
print(time.ctime())
    

