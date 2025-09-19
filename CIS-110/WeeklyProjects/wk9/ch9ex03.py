"""
Program Name : ch9ex03
Program description : Find the inner product of list input from user.
Author: Arthur Belanger
Date created: 4-3-25
Notes: I set the innerProd function up a little different than yours in class, I did it beforehand but got same result.
"""
import time

divider = ("_ _ _ ")
print(divider * 3)

def innerProd(x, y):
    prod = 0
    if len(x) != len(y):
        return 0 
    for i in range(len(x)):
        prod += x[i] * y[i]
    return prod

def main():
    x = eval(input("What is your first list: "))
    y = eval(input("What is your second list: "))
    print(f"The inner product is: {innerProd(x, y)}")
    
if __name__ == "__main__":
    main()

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - ch9ex03 ")
print(time.ctime())
    

