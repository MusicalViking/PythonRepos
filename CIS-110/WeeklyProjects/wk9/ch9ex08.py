"""
Program Name: ch9ex08
Program description: uses the sieve of eratosthenes formula to find prime numbers
Author: Arthur Belanger
Date created: 4-6-25
Notes: I really need to work on my math, I followed the formula and got the result that I feel is correct 
but I am not very confident for the math portion of this and I added a True statement for prime instead
of the .remove for the list. Getting [i for i, prime in enumerate(is_prime) if prime] correct took me a while.
"""
import time

divider = ("_ _ _ ")
print(divider * 3)

def sieve(n):
    if n < 2:
        return []
    yes = [True] * (n + 1)
    yes[0] = yes[1] = False
    p = 2
    while p * p <= n:
        if yes[p]:
            for multiple in range(p * p, n + 1, p):
                yes[multiple] = False
        p += 1
    return [i for i, prime in enumerate(yes) if prime]

def main():
    print("Sieve of Eratosthenes")
    n = int(input("Enter highest number: "))
    print(f"The prime #'s up to {n} are {sieve(n)}")

if __name__ == '__main__' : main()

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - ch9ex08 ")
print(time.ctime())
    

