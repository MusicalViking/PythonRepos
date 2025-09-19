"""
Program Name : ch7ex06
Program description : GCD calculator
Author: Arthur Belanger
Date created: 3-13-25
Notes: Greater Common Denominator

"""
print("--------------------------------")
import time

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("GCD Calculator!")
    n_1 = int(input("First number: "))
    n_2 = int(input("Second number: "))
    result = gcd(n_1, n_2)
    print(f"The GCD of {n_1} and {n_2} is: {result}")

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch7ex06")
print(time.ctime())
    

