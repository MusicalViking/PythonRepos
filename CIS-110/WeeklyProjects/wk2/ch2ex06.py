import time
#chex06
#Arthur Belanger
#Determine future values of an investment
#1-29-25
#
#--------------------------------

def main():
    print("This program calculates the future value of your investments")

    years = int(input("How many years would you like to calculate?: "))
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))

    for _ in range(years):
        principal = principal * (1 + apr)

    print(f"The value in {years} years is:", principal)

main()




#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())
