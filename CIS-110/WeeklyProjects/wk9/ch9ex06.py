"""
Program Name: ch9ex06
Program description: Converts list into integers
Author: Arthur Belanger
Date created: 4-5-25
Notes: I found this one to be pretty easy once I rememberd to use .split on the input, 
I don't fully understand how using eval() would make this code not work but I used 
.split() to seperate each input item wiith a space.
"""
import time

divider = ("_ _ _ ")
print(divider * 3)

def toNumbers(a):
    for i in range(len(a)):
        a[i] = float(a[i]) 

if __name__ == "__main__":

    b = input("What's your list to convert(separate with space): ")
    x = b.split()

    print(f"Before conversion: {x}")
    toNumbers(x)
    print(f"After conversion: {x}")  

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - ch9ex06 ")
print(time.ctime())
    


