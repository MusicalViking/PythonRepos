"""
Program Name: Program #5
Program Description: Figure out the shipping charges from a .CSV file.
Author: Arthur Belanger
Date Created: 3-17-25
Notes: The packages.csv file needs to be in the same folder of this to read it. I had a
hard time getting the file to work with the program and when I got it working I added
a try and except function to throw an error if it wasn't. I have beeen
using VS IDE for most of my programming as it was what I used for web dev but for some reason
this program would not read the file using VS or even Notepad++, it would only run in Idle.
I think it is from the way I have the enviroment set up but all is good.
"""
import time
import csv

def add_freight(weight):
    if weight < 16:
        return weight * 0.21
    elif weight < 32:
        return weight * 0.33
    elif weight < 64:
        return weight * 0.43
    else:
        return weight * 0.59

def hndl_track_fee(handling, tracking):
    if handling.lower() == 'yes' and tracking.lower() == 'yes':
        return 7.50
    elif handling.lower() == 'yes' or tracking.lower() == 'yes':
        return 5.00
    else:
        return 0.00

# read the package.csv file/this gave me a hard time
try:
    with open('packages.csv', 'r') as file:
        reader = csv.reader(file)
        packages = list(reader)
except FileNotFoundError:
    print("Error: file needs to be in the same folder as this program.")
    exit()

results = []
for package in packages:
    weight = float(package[0])
    freight_charge = add_freight(weight)
    add_fees = hndl_track_fee(package[1], package[2])
    total_shipping = freight_charge + add_fees
    results.append((weight, package[1], package[2], freight_charge, add_fees, total_shipping))

# print the results/pretty slick table if I might add :)I learned a lot more on the f strings this week.
# I think I am going to start using a seperator element on my code where it fits, I liked the way it came out.
header = f"{'Wt.(oz)-':<10}{'Handling-':<10}{'Tracking-':<10}{'Freight-':<10}{'H/T-':<10}{'Total':<10}"
seperator = "= = " * 14
print(header)
print(seperator)
for result in results:
    print(f"{result[0]:<10}{result[1]:<10}{result[2]:<10}{result[3]:<10.2f}{result[4]:<10.2f}{result[5]:<10.2f}")
    
print(seperator)
print("Arthur Belanger")
print("CIS-110 - Program #5")
print(time.ctime())
