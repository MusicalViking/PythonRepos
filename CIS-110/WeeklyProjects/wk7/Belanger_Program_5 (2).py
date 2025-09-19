"""
Program Name: Assignment #5
Program description
Author: Arthur Belanger
Date created: 

Notes:

"""
print("--------------------------------")
import time
import csv

packages = open('packages.csv','r')
for package in packages:
    weight, handling, tracking = package.strip().split(',')

# Define the cost per ounce based on weight
def calculate_freight_charge(weight):
    if weight < 16:
        return weight * 0.21
    elif weight < 32:
        return weight * 0.33
    elif weight < 64:
        return weight * 0.43
    else:
        return weight * 0.59

# Calculate the additional fees
def calculate_additional_fees(handling, tracking):
    if handling == 'yes' and tracking == 'yes':
        return 7.50
    elif handling == 'yes' or tracking == 'yes':
        return 5.00
    else:
        return 0.00

# Read the package data from the CSV file
with open('packages.csv', 'r') as file:
    reader = csv.reader(file)
    packages = list(reader)

# Calculate the total shipping charge for each package
results = []
for package in packages:
    weight = float(package[0])
    handling = package[1]
    tracking = package[2]
    
    freight_charge = calculate_freight_charge(weight)
    additional_fees = calculate_additional_fees(handling, tracking)
    total_shipping_charge = freight_charge + additional_fees
    
    results.append((weight, handling, tracking, freight_charge, additional_fees, total_shipping_charge))

# Print the results in a formatted table
print(f"{'Weight (oz)':<12}{'Handling':<10}{'Tracking':<10}{'Freight Charge':<15}{'Additional Fees':<15}{'Total Shipping Charge':<20}")
print("="*82)
for result in results:
    print(f"{result[0]:<12}{result[1]:<10}{result[2]:<10}{result[3]:<15.2f}{result[4]:<15.2f}{result[5]:<20.2f}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - Program # ")
print(time.ctime())
    

