import time
import math
#ch3ex16
#Arthur Belanger
#computes the fibonacci sequence that is input by user
#2-06-25
#In class exercise
#--------------------------------

print("To figure your fibonacci sequence number follow the steps below.")
print()
def main():
    num = int(input("Enter your fib number: "))

    a, b = 0, 1

    for _ in range(num):
        a, b = b, a + b
    print(f"The {num}th number is: {a}")

main()
            
#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())
