"""
Program Name : ch7ex01
Program description : Investment doubling calculator
Author: Arthur Belanger
Date created: 3-13-25
Notes: Figures the time it takes to double an investment.

"""
print("--------------------------------")
import time

def main():
    print("Welcome to your Investment Doubling Calculator, you'll be richer than a dwarve in no time!")
    
    apr = float(input("Enter your APR: "))
    principal = float(input("Enter your starting principal: "))  
    years = 0
    goal = principal * 2
    
    while principal < goal:
        principal = principal * (1 + apr)
        years += 1   
    print(f"It took {years} years to double the investment.")
    print(f"The final amount is ${principal:.2f}")

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 -ch7ex01 ")
print(time.ctime())
    

