"""
Program Name : ch6ex01
Program description : Calculates the pay of worked hours with overtime figured after 40.
Author: Arthur Belanger
Date created: 3-6-25
Notes:
"""
print("--------------------------------")
import time
def calculate_pay(worked, rate):
    normal = 40
    ot_multiplier = 1.5
    
    if worked > normal:
        ot_hours = worked - normal
        ot_pay = ot_hours * (rate * ot_multiplier)
        regular_pay = normal * rate
        total_pay = regular_pay + ot_pay
    else:
        total_pay = worked * rate 
    return total_pay

rate = float(input("Enter the hourly rate: "))
hours = float(input("Enter the number of hours worked: "))

total_pay = calculate_pay(hours, rate)
print(f"Total wages for the week: ${total_pay:.2f}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch6ex01 ")
print(time.ctime())
    

