"""
Program Name
Program description
Author: Arthur Belanger
Date created: 

Notes:

"""
print("--------------------------------")
import time


print("Welcome to the Python club")

name = input("What is your name? \n")

if name == "ben":
    evil_status = input("Are you evil? \n").lower()
    
    good_deeds = int(input("How many good deeds have you done today?\n"))
    
    if evil_status == "yes" and good_deeds < 4:
        print(f"You are not welcome here, {name} get out!\n")
    else:
        print(f"Hello {name} Welcome to the Python club\n")
       
else:
    print(f"Hello {name} Welcome to the Python club\n")


print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - Program # ")
print(time.ctime())
    

