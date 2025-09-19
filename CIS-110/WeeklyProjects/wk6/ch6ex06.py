"""
Program Name : ch6ex06
Program description ; Determines the amount to be paid for speeding ticket
Author: Arthur Belanger
Date created: 3-6-25
Notes: Learned some new stuff on the f strings and formatting output.
"""
print("--------------------------------")
import time

def calculate_fine(speed, clocked):
    base = 50
    additional_per_mph = 5
    over_90 = 200
    
    if clocked <= speed:
        return "Speed is legal."
    
    over_speed = clocked - speed
    fine = base + (over_speed * additional_per_mph)
    
    if clocked > 90:
        fine += over_90    
    return f"The fine is ${fine:.2f}, SLOW DOWN!!!"

speed = float(input("Enter the speed limit: "))
clocked = float(input("Enter the clocked speed: "))
result = calculate_fine(speed, clocked)
print(result)

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch6ex06 ")
print(time.ctime())
    

