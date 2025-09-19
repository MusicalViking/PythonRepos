"""
Program Name : ch8ex11
Program description : calculate the return on a investment over input amout of years and interest
Author: Arthur Belanger
Date created: 3-27-25
Notes:

"""
print("--------------------------------")
import time

def future_value_table():
    try:
        principal = float(input("Enter the initial amount : $"))
        apr = float(input("Enter the annual rate : "))
        years = int(input("Enter the number of years you want the value on : "))

        if principal < 0 or apr < 0 or years < 0:
            raise ValueError("Investment amount, interest rate, and years must be positive.")
        print("\nYear | Future Value")
        print("-------------------")
        for year in range(years + 1):
            future_value = principal * (1 + apr) ** year
            print(f"{year:4} | ${future_value:11.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

future_value_table()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch8ex11 ")
print(time.ctime())
    

