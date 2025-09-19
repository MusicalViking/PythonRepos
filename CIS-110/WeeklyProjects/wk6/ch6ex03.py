"""
Program Name
Program description
Author: Arthur Belanger
Date created: 

Notes:

"""
print("--------------------------------")
import time

def main():
    print("Exam grader\n")
    score = int(input("What is the score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"The lettergrade is : {grade}")


print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - Program # ")
print(time.ctime())
    

