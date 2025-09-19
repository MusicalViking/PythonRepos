"""
Program Name ; ch7exA
Program description : Accumulator program
Author: Arthur Belanger
Date created: 3-13-25
Notes:

"""
print("--------------------------------")
import time

def main():
    print("Accumulator Program!")
    total = 0

    while total < 100:
        while True:
            value = float(input("Enter a positive number: "))
            if value > 0:
                break
            else:
                print("Enter a number larger than 0 please.")
        total += value
        print(f"Current total: {total}")
    print(f"Final total: {total}")

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch7exA")
print(time.ctime())
    

